---
language:
- tr
license: apache-2.0
task_categories:
- question-answering
pretty_name: LangUsta KPSS Reasoning
size_categories:
- n<1K
---

# LangUsta KPSS Reasoning

Bu veri seti `AhmetSemih/Deepseek-mcq-reasoning-dataset` içindeki yalnızca `KPSS` ve
`KPSS Denemeleri` bölümlerinden hazırlanmıştır. 21 kaydın soru, seçenek, thinking ve response
alanları korunmuştur.

## Şema

Hocanın referans veri setiyle uyumlu olarak her kayıtta `train` adlı tek sütun bulunur. Bu sütun,
`content`, `images`, `role`, `thinking` ve `tool_calls` alanlarını taşıyan user/assistant mesaj listesidir.
Veri deterministik olarak train/test bölümlerine ayrılmıştır.

## Kaynak ve lisans

- Kaynak: https://huggingface.co/datasets/AhmetSemih/Deepseek-mcq-reasoning-dataset
- Kaynak sorular: `alibayram/turkish_mmlu`
- Lisans: Apache 2.0

Bu depo orijinal veri setinin yerine geçmez; kullanımda kaynak atfı korunmalıdır.
