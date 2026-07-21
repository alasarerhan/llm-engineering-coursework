---
language:
- tr
license: mit
task_categories:
- text-generation
tags:
- identity-finetuning
- kpss
- langusta
---

# LangUsta Kimlik Veri Seti

LangUsta'nın adını, yaratıcısını ve görevini öğretmek için hazırlanmıştır. Kimlik tanımı:
“Erhan Alasar tarafından oluşturulan, Türkçe KPSS sorularını gerekçeli açıklayan eğitim destek asistanı.”

Veri, elle yazılmış ve kontrol edilmiş 20 çekirdek kimlik soru-cevap örneğinin deterministik soru
varyasyonlarıyla 100 kayda genişletilmesiyle oluşur. Harici üretken model veya API kullanılmamıştır.
Her kayıt, referans veri setiyle uyumlu `train` sütununda user/assistant mesaj listesi taşır.
