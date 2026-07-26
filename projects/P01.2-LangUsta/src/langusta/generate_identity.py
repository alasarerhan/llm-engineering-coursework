"""20 elle yazılmış LangUsta kimlik örneğini doğrular ve DatasetDict üretir."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from datasets import Dataset, DatasetDict

from .format_adapter import clean_text, to_reference_record, validate_messages
from .prepare_dataset import stable_id
from .settings import IDENTITY_DATASET_REPO, IDENTITY_SYSTEM_PROMPT


def load_manual(path: Path) -> list[dict[str, str]]:
    examples = json.loads(path.read_text(encoding="utf-8"))
    if len(examples) < 20:
        raise ValueError("Kimlik projesi için en az 20 manuel örnek gerekir.")
    cleaned = []
    for item in examples:
        question = clean_text(item.get("question"))
        answer = clean_text(item.get("answer"))
        if not question or not answer:
            raise ValueError("Manuel kimlik örneklerinde boş soru/cevap olamaz.")
        cleaned.append({"question": question, "answer": answer, "generation_method": "manual"})
    return cleaned


def build_dataset(examples: list[dict[str, str]]) -> DatasetDict:
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in examples:
        question_key = item["question"].casefold()
        if question_key in seen:
            continue
        seen.add(question_key)
        record = to_reference_record(
            item["question"],
            item["answer"],
            source="manual",
            record_id=stable_id(item["question"], item["answer"]),
            system_prompt=IDENTITY_SYSTEM_PROMPT,
        )
        record["generation_method"] = "manual"
        if validate_messages(record["messages"]):
            records.append(record)
    records.sort(key=lambda item: item["id"])
    test_size = max(1, round(len(records) * 0.1))
    return DatasetDict(
        {"train": Dataset.from_list(records[test_size:]), "test": Dataset.from_list(records[:test_size])}
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manual", type=Path, default=Path("data/manual_identity.json"))
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/identity_dataset"))
    parser.add_argument("--push", action="store_true")
    parser.add_argument("--repo-id", default=IDENTITY_DATASET_REPO)
    args = parser.parse_args()

    dataset = build_dataset(load_manual(args.manual))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, split in dataset.items():
        split.to_json(args.output_dir / f"{name}.jsonl", force_ascii=False)
    print({name: len(split) for name, split in dataset.items()})
    if args.push:
        dataset.push_to_hub(args.repo_id, private=False)


if __name__ == "__main__":
    main()
