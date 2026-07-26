"""Türkçe KPSS akıl yürütme verisini temizler, böler ve Hub'a hazırlar."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable, Mapping, Any

from datasets import Dataset, DatasetDict, load_dataset

from .format_adapter import clean_text, to_reference_record, validate_messages
from .settings import MAIN_DATASET_REPO, SOURCE_DATASET


def stable_id(question: str, response: str) -> str:
    return hashlib.sha256(f"{question}\n{response}".encode("utf-8")).hexdigest()[:16]


def convert_rows(
    rows: Iterable[Mapping[str, Any]],
    *,
    max_question_chars: int = 2_000,
    max_response_chars: int = 4_000,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    """Yalnızca KPSS bölümlerini temizleyip akıl yürütme kayıtlarına dönüştürür."""
    records: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    stats = {"input": 0, "kept": 0, "non_kpss": 0, "empty": 0, "too_long": 0, "duplicate": 0}

    for row in rows:
        stats["input"] += 1
        if clean_text(row.get("section")).casefold() not in {"kpss", "kpss denemeleri"}:
            stats["non_kpss"] += 1
            continue
        question = clean_text(row.get("question"))
        options = [clean_text(option) for option in (row.get("options") or []) if clean_text(option)]
        if options:
            question += "\n\nSeçenekler:\n" + "\n".join(
                f"{index + 1}. {option}" for index, option in enumerate(options)
            )
        thinking = clean_text(row.get("thinking"))
        response = clean_text(row.get("response"))
        if not question or not thinking or not response:
            stats["empty"] += 1
            continue
        if len(question) > max_question_chars or len(response) > max_response_chars:
            stats["too_long"] += 1
            continue
        key = (question.casefold(), response.casefold())
        if key in seen:
            stats["duplicate"] += 1
            continue
        seen.add(key)
        record = to_reference_record(
            question,
            f"<think>\n{thinking}\n</think>\n{response}",
            source=SOURCE_DATASET,
            record_id=stable_id(question, response),
        )
        record.update({"question": question, "thinking": thinking, "response": response})
        if validate_messages(record["messages"]):
            records.append(record)

    records.sort(key=lambda item: item["id"])
    stats["kept"] = len(records)
    return records, stats


def split_records(records: list[dict[str, Any]], test_ratio: float = 0.1) -> DatasetDict:
    """Hash sıralamasından deterministik train/test ayrımı üretir."""
    if len(records) < 2:
        raise ValueError("Train/test ayrımı için en az iki geçerli kayıt gerekir.")
    records = sorted(records, key=lambda item: item["id"])
    test_size = max(1, round(len(records) * test_ratio))
    test = records[:test_size]
    train = records[test_size:]
    return DatasetDict({"train": Dataset.from_list(train), "test": Dataset.from_list(test)})


def save_outputs(dataset: DatasetDict, output_dir: Path, stats: dict[str, int]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for split_name, split in dataset.items():
        split.to_json(output_dir / f"{split_name}.jsonl", force_ascii=False)
    with (output_dir / "corpus.txt").open("w", encoding="utf-8") as corpus:
        for split in dataset.values():
            for item in split:
                corpus.write(item["messages"][1]["content"] + "\n")
                corpus.write(item["messages"][2]["content"] + "\n")
    (output_dir / "stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def to_hub_dataset(dataset: DatasetDict) -> DatasetDict:
    """Dahili DatasetDict'i referans Hub şemasına dönüştürür."""
    return DatasetDict(
        {
            split_name: Dataset.from_list(
                [
                    {
                        "train": [
                            {"content": item["question"], "images": None, "role": "user", "thinking": None, "tool_calls": None},
                            {"content": item["response"], "images": None, "role": "assistant", "thinking": item["thinking"], "tool_calls": None},
                        ]
                    }
                    for item in split
                ]
            )
            for split_name, split in dataset.items()
        }
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/main_dataset"))
    parser.add_argument("--push", action="store_true", help="Hazırlanan DatasetDict'i Hub'a yükle")
    parser.add_argument("--repo-id", default=MAIN_DATASET_REPO)
    parser.add_argument("--token", default=None, help="Tercihen HF_TOKEN ortam değişkenini kullanın")
    args = parser.parse_args()

    source = load_dataset(SOURCE_DATASET, split="train")
    records, stats = convert_rows(source)
    dataset = split_records(records)
    save_outputs(dataset, args.output_dir, stats)
    print(json.dumps({"splits": {k: len(v) for k, v in dataset.items()}, **stats}, indent=2))

    if args.push:
        to_hub_dataset(dataset).push_to_hub(args.repo_id, token=args.token, private=False)
        print(f"Yüklendi: https://huggingface.co/datasets/{args.repo_id}")


if __name__ == "__main__":
    main()
