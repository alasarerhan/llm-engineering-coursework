"""Kaynak kayıtlarını tek noktadan sohbet formatına dönüştürür.

Yayın şeması hocanın ``identity_finetune_magibu_q3`` veri setiyle eşleştirilmiştir.
"""

from __future__ import annotations

from typing import Any

from .settings import SYSTEM_PROMPT


def clean_text(value: Any) -> str:
    """Metni güvenli biçimde normalize eder."""
    if value is None:
        return ""
    return " ".join(str(value).replace("\x00", " ").split()).strip()


def to_messages(question: str, response: str, system_prompt: str = SYSTEM_PROMPT) -> list[dict[str, str]]:
    """Soru-cevap çiftini standart ChatML-benzeri mesaj listesine çevirir."""
    return [
        {"role": "system", "content": clean_text(system_prompt)},
        {"role": "user", "content": clean_text(question)},
        {"role": "assistant", "content": clean_text(response)},
    ]


def to_reference_record(
    question: str,
    response: str,
    *,
    source: str,
    record_id: str,
    system_prompt: str = SYSTEM_PROMPT,
) -> dict[str, Any]:
    """Temizleme ve eğitim sırasında kullanılan izlenebilir dahili kayıt."""

    return {
        "id": record_id,
        "messages": to_messages(question, response, system_prompt),
        "source": source,
    }


def to_hub_record(messages: list[dict[str, str]]) -> dict[str, Any]:
    """Mesajları hocanın tek ``train`` sütunlu Hub şemasına dönüştürür."""
    return {
        "train": [
            {
                "content": message["content"],
                "images": None,
                "role": message["role"],
                "thinking": "" if message["role"] == "assistant" else None,
                "tool_calls": None,
            }
            for message in messages
            if message["role"] in {"user", "assistant"}
        ]
    }


def validate_messages(messages: Any) -> bool:
    """Bir mesaj listesinin beklenen üç rolü ve dolu içerikleri taşıdığını denetler."""
    if not isinstance(messages, list) or len(messages) != 3:
        return False
    expected = ("system", "user", "assistant")
    return all(
        isinstance(message, dict)
        and message.get("role") == role
        and isinstance(message.get("content"), str)
        and bool(message["content"].strip())
        for message, role in zip(messages, expected)
    )
