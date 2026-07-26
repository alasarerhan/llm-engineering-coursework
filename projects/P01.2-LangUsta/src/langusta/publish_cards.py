"""Hazır Hub depolarına açıklayıcı dataset/model kartlarını yükler."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import HfApi, get_token

from .settings import (
    IDENTITY_ADAPTER_REPO,
    IDENTITY_DATASET_REPO,
    MAIN_ADAPTER_REPO,
    MAIN_DATASET_REPO,
    TOKENIZER_REPO,
)

CARDS = {
    MAIN_DATASET_REPO: ("dataset", "main_dataset.md"),
    TOKENIZER_REPO: ("model", "tokenizer.md"),
    MAIN_ADAPTER_REPO: ("model", "main_adapter.md"),
    IDENTITY_DATASET_REPO: ("dataset", "identity_dataset.md"),
    IDENTITY_ADAPTER_REPO: ("model", "identity_adapter.md"),
}


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--only",
        choices=("main-dataset", "tokenizer", "main-adapter", "identity-dataset", "identity-adapter"),
        action="append",
        help="Yalnızca seçilen hazır depoların kartını yükle; birden fazla kez kullanılabilir.",
    )
    args = parser.parse_args()
    token = os.getenv("HF_TOKEN") or get_token()
    if not token:
        raise RuntimeError("HF_TOKEN .env içinde veya Hugging Face oturumunda bulunamadı.")
    api = HfApi(token=token)
    cards_dir = Path("cards")
    labels = {
        "main-dataset": MAIN_DATASET_REPO,
        "tokenizer": TOKENIZER_REPO,
        "main-adapter": MAIN_ADAPTER_REPO,
        "identity-dataset": IDENTITY_DATASET_REPO,
        "identity-adapter": IDENTITY_ADAPTER_REPO,
    }
    selected = {labels[label] for label in args.only} if args.only else set(CARDS)
    for repo_id, (repo_type, filename) in CARDS.items():
        if repo_id not in selected:
            continue
        api.upload_file(
            path_or_fileobj=cards_dir / filename,
            path_in_repo="README.md",
            repo_id=repo_id,
            repo_type=repo_type,
            commit_message="Add LangUsta repository card",
        )
        print(f"Kart yüklendi: {repo_id}")


if __name__ == "__main__":
    main()
