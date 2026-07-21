from pathlib import Path

from langusta.generate_identity import build_dataset, load_manual


def test_manual_identity_has_required_facts():
    examples = load_manual(Path("data/manual_identity.json"))
    assert len(examples) == 20
    joined = " ".join(item["answer"] for item in examples)
    assert "LangUsta" in joined
    assert "Erhan Alasar" in joined
    assert "KPSS" in joined


def test_manual_identity_builds_valid_splits():
    dataset = build_dataset(load_manual(Path("data/manual_identity.json")))
    assert len(dataset["train"]) == 18
    assert len(dataset["test"]) == 2
    assert set(dataset["train"].column_names) == {
        "id", "messages", "source", "generation_method"
    }
