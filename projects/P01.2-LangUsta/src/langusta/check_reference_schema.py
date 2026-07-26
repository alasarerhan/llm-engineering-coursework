"""Hocanın erişim kısıtlı veri setinin şemasını yayın öncesinde karşılaştırır."""

from __future__ import annotations

import json

from datasets import load_dataset

from .settings import REFERENCE_DATASET


def main() -> None:
    dataset = load_dataset(REFERENCE_DATASET)
    report = {
        "dataset": REFERENCE_DATASET,
        "subsets_or_splits": list(dataset.keys()),
        "features": {name: str(split.features) for name, split in dataset.items()},
        "sample_keys": {name: list(split[0].keys()) for name, split in dataset.items() if len(split)},
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print("Bu çıktı format_adapter.py içindeki to_reference_record ile karşılaştırılmalıdır.")


if __name__ == "__main__":
    main()

