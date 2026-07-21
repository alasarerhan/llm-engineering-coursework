# LLM Engineering Coursework

Bu depo, büyük dil modellerinin veri hazırlığından tokenizer eğitimine, sıfırdan model geliştirmeden LoRA fine-tuning süreçlerine kadar uzanan kurs çalışmalarını bir araya getirir.

## Projeler

| Proje | Kapsam | Çıktılar |
| --- | --- | --- |
| [LangUsta](projects/langusta/) | KPSS verisi hazırlama, byte-level BPE tokenizer, Qwen2.5 QLoRA ve kimlik fine-tuning | Hugging Face dataset, tokenizer ve LoRA adaptörleri |
| [Turkish District LM](projects/turkish-district-lm/) | BPE tokenizer ve decoder-only Transformer ile sıfırdan dil modeli eğitimi | Eğitim kodu, veri ve inference aracı |

## Kapsanan Konular

- Veri toplama, temizleme ve eğitim/test ayrımı
- BPE tokenizer tasarımı ve eğitimi
- Decoder-only Transformer bileşenleri
- Nedensel dil modeli eğitimi ve metin üretimi
- QLoRA/LoRA ile instruction fine-tuning
- Hugging Face üzerinde model ve veri seti yayınlama

Her proje kendi kurulum, kullanım, veri kaynağı ve teknik kararlarını içeren bağımsız bir README dosyasına sahiptir.

## Lisans

Bu depodaki özgün proje kodları [MIT Lisansı](LICENSE) ile sunulmaktadır. Veri setleri ve kurs tarafından sağlanan başlangıç kodları için ilgili proje belgelerinde belirtilen kaynak ve kullanım koşulları geçerlidir.
