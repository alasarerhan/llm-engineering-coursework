# P01.2 — LangUsta

LangUsta, KPSS sorularını Türkçe ve gerekçeli biçimde çözmek üzere Qwen2.5-0.5B-Instruct üzerinde geliştirilen,
yeniden üretilebilir bir veri hazırlama, tokenizer eğitimi ve QLoRA uyarlama projesidir.

## Proje Çıktıları

| Çıktı | Hugging Face deposu |
|---|---|
| KPSS akıl yürütme veri seti | [`erhanalsr/langusta-kpss-reasoning`](https://huggingface.co/datasets/erhanalsr/langusta-kpss-reasoning) |
| Byte-level BPE tokenizer | [`erhanalsr/langusta-kpss-bpe-tokenizer`](https://huggingface.co/erhanalsr/langusta-kpss-bpe-tokenizer) |
| KPSS LoRA adaptörü | [`erhanalsr/langusta-kpss-lora`](https://huggingface.co/erhanalsr/langusta-kpss-lora) |
| LangUsta kimlik veri seti | [`erhanalsr/langusta-identity`](https://huggingface.co/datasets/erhanalsr/langusta-identity) |
| LangUsta kimlik LoRA adaptörü | [`erhanalsr/langusta-identity-lora`](https://huggingface.co/erhanalsr/langusta-identity-lora) |

Tüm Hugging Face çıktıları yayımlanmış ve erişime açıktır.

## Yöntem

Ana veri seti, Apache 2.0 lisanslı
[`AhmetSemih/Deepseek-mcq-reasoning-dataset`](https://huggingface.co/datasets/AhmetSemih/Deepseek-mcq-reasoning-dataset)
veri setinin yalnızca `KPSS` ve `KPSS Denemeleri` bölümlerinden hazırlanır. Soru, seçenekler,
`thinking` ve `response` alanları korunur; veriler deterministik olarak train/test kümelerine
ayrılır. Yayınlanan kayıtlar hocanın `alibayram/identity_finetune_magibu_q3` veri setiyle aynı şekilde,
`train` sütununda `content`, `images`, `role`, `thinking` ve `tool_calls` alanlı mesaj listeleri taşır.

Filtre sonucunda 21 KPSS kaydı elde edilir; ayrıca `kpss_reasoning.jsonl` dosyasına kaydedilir.
Kimlik eğitimi için 20 örnek elle hazırlanır ve yalnızca deterministik soru kalıplarıyla 100 kayda
genişletilir. Harici üretken model veya sentetik veri API'si kullanılmaz.

Her iki adaptör de `Qwen/Qwen2.5-0.5B-Instruct` üzerinde Unsloth 4-bit QLoRA ile bağımsız olarak
eğitilir. Özel BPE tokenizer ayrı bir proje çıktısıdır; LoRA eğitimlerinde temel modelin kendi
tokenizerı kullanılır.

## Çalıştırma

1. [LangUsta.ipynb](notebooks/LangUsta.ipynb) dosyasını Kaggle'a notebook olarak aktarın.
2. Notebook ayarlarından internet erişimini açın ve GPU T4 accelerator seçin.
3. Kaggle notebook ayarlarındaki Secrets bölümüne `HF_TOKEN` adıyla write yetkili tokenı ekleyin.
4. Secret erişimini notebook için etkinleştirin.
5. Notebook'u baştan sona çalıştırın.

Notebook veri setlerini, tokenizerı ve iki LoRA adaptörünü üretir; kabul kontrolleri geçtikten sonra
beş çıktıyı Hugging Face Hub'a otomatik olarak yükler.

## Yerel Testler

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[test]'
pytest -q
```

## Proje Yapısı

```text
├── notebooks/LangUsta.ipynb        # Uçtan uca Kaggle/Colab iş akışı
├── src/langusta/                    # Veri, tokenizer ve yayın yardımcıları
├── data/manual_identity.json        # Elle hazırlanmış 20 kimlik örneği
├── cards/                           # Hugging Face veri/model kartları
├── tests/                           # Veri ve notebook doğrulama testleri
├── .env.example                     # Gizli bilgi içermeyen ortam şablonu
└── ../../LICENSE                    # Depo genelindeki MIT lisansı
```

## Kaynak ve Lisans

- AhmetSemih DeepSeek MCQ Reasoning Dataset: Apache 2.0; kaynak sorular `alibayram/turkish_mmlu`.
- Bu projedeki özgün kod: MIT License, © 2026 Erhan Alasar.
