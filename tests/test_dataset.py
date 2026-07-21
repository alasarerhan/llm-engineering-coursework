from langusta.format_adapter import to_hub_record, validate_messages
from langusta.prepare_dataset import convert_rows, split_records


def test_convert_filters_invalid_and_duplicate_rows():
    rows = [
        {"section": "KPSS", "question": " Soru? ", "thinking": " Düşünme ", "response": " Cevap. "},
        {"section": "KPSS", "question": "soru?", "thinking": "Düşünme", "response": "cevap."},
        {"section": "TUS", "question": "TUS", "thinking": "D", "response": "C"},
        {"section": "KPSS", "question": "", "thinking": "D", "response": "eksik"},
        {"section": "KPSS", "question": "x" * 2001, "thinking": "D", "response": "uzun"},
        {"section": "KPSS Denemeleri", "question": "Diğer soru?", "thinking": "Gerekçe", "response": "Yanıt"},
    ]
    records, stats = convert_rows(rows)
    assert len(records) == 2
    assert stats == {"input": 6, "kept": 2, "non_kpss": 1, "empty": 1, "too_long": 1, "duplicate": 1}
    assert all(validate_messages(record["messages"]) for record in records)
    assert all(record["thinking"] for record in records)


def test_split_is_deterministic_and_disjoint():
    rows = [
        {"section": "KPSS", "question": f"Soru {i}", "thinking": f"Gerekçe {i}", "response": f"Cevap {i}"}
        for i in range(20)
    ]
    records, _ = convert_rows(rows)
    first = split_records(records)
    second = split_records(list(reversed(records)))
    assert first["train"]["id"] == second["train"]["id"]
    assert first["test"]["id"] == second["test"]["id"]
    assert set(first["train"]["id"]).isdisjoint(first["test"]["id"])
    assert len(first["test"]) == 2


def test_hub_schema_matches_reference_dataset():
    record = to_hub_record(
        [
            {"role": "system", "content": "System"},
            {"role": "user", "content": "Question"},
            {"role": "assistant", "content": "Answer"},
        ]
    )
    assert list(record) == ["train"]
    assert [message["role"] for message in record["train"]] == ["user", "assistant"]
    assert set(record["train"][0]) == {"content", "images", "role", "thinking", "tool_calls"}
