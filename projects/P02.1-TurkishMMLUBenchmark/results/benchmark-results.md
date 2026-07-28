# TR-MMLU Benchmark Results

Qwen2.5-0.5B-Instruct temel modeli ile LangUsta KPSS LoRA adaptörünün
aynı Türkçe MMLU soruları üzerindeki karşılaştırmalı sonuçlarıdır.

## Evaluation Setup

- Benchmark: [TR-MMLU](https://github.com/malibayram/llm-tr-benchmarks)
- Evaluated questions: 6,200
- Decoding: deterministic greedy generation
- Maximum new tokens: 42
- Answer evaluation: exact option matching with semantic fallback

## Overall Results

| Model | Correct | Questions | Accuracy | Duration |
| --- | ---: | ---: | ---: | ---: |
| Qwen2.5-0.5B-Instruct | 1,767 | 6,200 | 28.50% | 1599.652 s |
| LangUsta-KPSS-LoRA | 1,258 | 6,200 | 20.29% | 6884.318 s |

## Results by Section

| Model | Section | Correct | Questions | Accuracy |
| --- | --- | ---: | ---: | ---: |
| Qwen2.5-0.5B-Instruct | AUZEF | 34 | 100 | 34.00% |
| Qwen2.5-0.5B-Instruct | Acil Durum ve Afet Yönetimi | 37 | 100 | 37.00% |
| Qwen2.5-0.5B-Instruct | Adalet | 24 | 100 | 24.00% |
| Qwen2.5-0.5B-Instruct | Aşçılık | 29 | 100 | 29.00% |
| Qwen2.5-0.5B-Instruct | Bankacılık ve Sigortacılık | 25 | 100 | 25.00% |
| Qwen2.5-0.5B-Instruct | Büro Yönetimi ve Yönetici Asistanlığı | 30 | 100 | 30.00% |
| Qwen2.5-0.5B-Instruct | DHBT | 27 | 100 | 27.00% |
| Qwen2.5-0.5B-Instruct | Dini Bilgiler | 22 | 100 | 22.00% |
| Qwen2.5-0.5B-Instruct | Dış Ticaret | 26 | 100 | 26.00% |
| Qwen2.5-0.5B-Instruct | Ehliyet Sınavı | 29 | 100 | 29.00% |
| Qwen2.5-0.5B-Instruct | Elektrik Enerjisi Üretim,İletim ve Dağıtımı | 33 | 100 | 33.00% |
| Qwen2.5-0.5B-Instruct | Emlak ve Emlak Yönetimi | 30 | 100 | 30.00% |
| Qwen2.5-0.5B-Instruct | Ev İdaresi | 28 | 100 | 28.00% |
| Qwen2.5-0.5B-Instruct | Felsefe | 23 | 100 | 23.00% |
| Qwen2.5-0.5B-Instruct | Fotoğrafçılık ve Kameramanlık | 27 | 100 | 27.00% |
| Qwen2.5-0.5B-Instruct | Futbol | 32 | 100 | 32.00% |
| Qwen2.5-0.5B-Instruct | Halkla İlişkiler ve Reklamcılık | 30 | 100 | 30.00% |
| Qwen2.5-0.5B-Instruct | Halkla İlişkiler ve Tanıtım | 28 | 100 | 28.00% |
| Qwen2.5-0.5B-Instruct | Havacılık Yönetimi | 21 | 100 | 21.00% |
| Qwen2.5-0.5B-Instruct | KPSS | 19 | 100 | 19.00% |
| Qwen2.5-0.5B-Instruct | KPSS Denemeleri | 29 | 100 | 29.00% |
| Qwen2.5-0.5B-Instruct | Kamu Yönetimi | 25 | 100 | 25.00% |
| Qwen2.5-0.5B-Instruct | Kim 500 Milyar İster | 28 | 100 | 28.00% |
| Qwen2.5-0.5B-Instruct | Kültürel Miras ve Turizm | 23 | 100 | 23.00% |
| Qwen2.5-0.5B-Instruct | Laborant ve Veteriner Sağlık | 24 | 100 | 24.00% |
| Qwen2.5-0.5B-Instruct | Lojistik | 24 | 100 | 24.00% |
| Qwen2.5-0.5B-Instruct | Maliye | 31 | 100 | 31.00% |
| Qwen2.5-0.5B-Instruct | Marka İletişimi | 19 | 100 | 19.00% |
| Qwen2.5-0.5B-Instruct | Medya ve İletişim | 32 | 100 | 32.00% |
| Qwen2.5-0.5B-Instruct | Menkul Kıymetler ve Sermaye Piyasası | 28 | 100 | 28.00% |
| Qwen2.5-0.5B-Instruct | Muhasebe ve Vergi Uygulamaları | 33 | 100 | 33.00% |
| Qwen2.5-0.5B-Instruct | Okul Öncesi Öğretmenliği | 28 | 100 | 28.00% |
| Qwen2.5-0.5B-Instruct | Parakende Satış ve Mağaza Yöneticiliği | 21 | 100 | 21.00% |
| Qwen2.5-0.5B-Instruct | Radyo ve Televizyon Programcılığı | 31 | 100 | 31.00% |
| Qwen2.5-0.5B-Instruct | Sağlık Kurumları İşletmeciliği | 36 | 100 | 36.00% |
| Qwen2.5-0.5B-Instruct | Sağlık Yönetimi | 29 | 100 | 29.00% |
| Qwen2.5-0.5B-Instruct | Siyer | 28 | 100 | 28.00% |
| Qwen2.5-0.5B-Instruct | Sosyal Hizmet | 32 | 100 | 32.00% |
| Qwen2.5-0.5B-Instruct | Sosyal Hizmetler | 31 | 100 | 31.00% |
| Qwen2.5-0.5B-Instruct | Sosyoloji | 29 | 100 | 29.00% |
| Qwen2.5-0.5B-Instruct | Spor Yönetimi | 33 | 100 | 33.00% |
| Qwen2.5-0.5B-Instruct | TUS | 26 | 100 | 26.00% |
| Qwen2.5-0.5B-Instruct | Tarih | 30 | 100 | 30.00% |
| Qwen2.5-0.5B-Instruct | Tarım | 28 | 100 | 28.00% |
| Qwen2.5-0.5B-Instruct | Turizm ve Otel İşletmeciliği | 34 | 100 | 34.00% |
| Qwen2.5-0.5B-Instruct | Turizm ve Seyehat Hizmetleri | 35 | 100 | 35.00% |
| Qwen2.5-0.5B-Instruct | Türk Dili ve Edebiyatı | 24 | 100 | 24.00% |
| Qwen2.5-0.5B-Instruct | Tıbbi Dökümantasyon ve Sekreterlik | 33 | 100 | 33.00% |
| Qwen2.5-0.5B-Instruct | Uluslar Arası İlişkiler | 22 | 100 | 22.00% |
| Qwen2.5-0.5B-Instruct | Uluslararası Ticaret ve Lojistik Yönetimi | 31 | 100 | 31.00% |
| Qwen2.5-0.5B-Instruct | Yaşlı Bakımı | 27 | 100 | 27.00% |
| Qwen2.5-0.5B-Instruct | Yerel Yönetimler | 33 | 100 | 33.00% |
| Qwen2.5-0.5B-Instruct | Yönetim Bİlişim Sistemleri | 25 | 100 | 25.00% |
| Qwen2.5-0.5B-Instruct | Çalışma Ekonomisi ve Endüstri İlişkileri | 34 | 100 | 34.00% |
| Qwen2.5-0.5B-Instruct | Çağrı Merkezi Hizmetleri | 25 | 100 | 25.00% |
| Qwen2.5-0.5B-Instruct | Çocuk Gelişimi | 31 | 100 | 31.00% |
| Qwen2.5-0.5B-Instruct | Özel Koruma ve Güvenlik | 24 | 100 | 24.00% |
| Qwen2.5-0.5B-Instruct | Üniversite Giriş Sınavı Temel Bilimler | 24 | 100 | 24.00% |
| Qwen2.5-0.5B-Instruct | İktisat | 30 | 100 | 30.00% |
| Qwen2.5-0.5B-Instruct | İlahiyat | 31 | 100 | 31.00% |
| Qwen2.5-0.5B-Instruct | İnsan Kaynakları Yönetimi | 36 | 100 | 36.00% |
| Qwen2.5-0.5B-Instruct | İşletme Yönetimi | 36 | 100 | 36.00% |
| LangUsta-KPSS-LoRA | AUZEF | 23 | 100 | 23.00% |
| LangUsta-KPSS-LoRA | Acil Durum ve Afet Yönetimi | 24 | 100 | 24.00% |
| LangUsta-KPSS-LoRA | Adalet | 15 | 100 | 15.00% |
| LangUsta-KPSS-LoRA | Aşçılık | 20 | 100 | 20.00% |
| LangUsta-KPSS-LoRA | Bankacılık ve Sigortacılık | 20 | 100 | 20.00% |
| LangUsta-KPSS-LoRA | Büro Yönetimi ve Yönetici Asistanlığı | 25 | 100 | 25.00% |
| LangUsta-KPSS-LoRA | DHBT | 19 | 100 | 19.00% |
| LangUsta-KPSS-LoRA | Dini Bilgiler | 13 | 100 | 13.00% |
| LangUsta-KPSS-LoRA | Dış Ticaret | 19 | 100 | 19.00% |
| LangUsta-KPSS-LoRA | Ehliyet Sınavı | 16 | 100 | 16.00% |
| LangUsta-KPSS-LoRA | Elektrik Enerjisi Üretim,İletim ve Dağıtımı | 16 | 100 | 16.00% |
| LangUsta-KPSS-LoRA | Emlak ve Emlak Yönetimi | 22 | 100 | 22.00% |
| LangUsta-KPSS-LoRA | Ev İdaresi | 20 | 100 | 20.00% |
| LangUsta-KPSS-LoRA | Felsefe | 22 | 100 | 22.00% |
| LangUsta-KPSS-LoRA | Fotoğrafçılık ve Kameramanlık | 21 | 100 | 21.00% |
| LangUsta-KPSS-LoRA | Futbol | 26 | 100 | 26.00% |
| LangUsta-KPSS-LoRA | Halkla İlişkiler ve Reklamcılık | 23 | 100 | 23.00% |
| LangUsta-KPSS-LoRA | Halkla İlişkiler ve Tanıtım | 19 | 100 | 19.00% |
| LangUsta-KPSS-LoRA | Havacılık Yönetimi | 20 | 100 | 20.00% |
| LangUsta-KPSS-LoRA | KPSS | 16 | 100 | 16.00% |
| LangUsta-KPSS-LoRA | KPSS Denemeleri | 21 | 100 | 21.00% |
| LangUsta-KPSS-LoRA | Kamu Yönetimi | 18 | 100 | 18.00% |
| LangUsta-KPSS-LoRA | Kim 500 Milyar İster | 12 | 100 | 12.00% |
| LangUsta-KPSS-LoRA | Kültürel Miras ve Turizm | 25 | 100 | 25.00% |
| LangUsta-KPSS-LoRA | Laborant ve Veteriner Sağlık | 20 | 100 | 20.00% |
| LangUsta-KPSS-LoRA | Lojistik | 16 | 100 | 16.00% |
| LangUsta-KPSS-LoRA | Maliye | 18 | 100 | 18.00% |
| LangUsta-KPSS-LoRA | Marka İletişimi | 21 | 100 | 21.00% |
| LangUsta-KPSS-LoRA | Medya ve İletişim | 15 | 100 | 15.00% |
| LangUsta-KPSS-LoRA | Menkul Kıymetler ve Sermaye Piyasası | 19 | 100 | 19.00% |
| LangUsta-KPSS-LoRA | Muhasebe ve Vergi Uygulamaları | 32 | 100 | 32.00% |
| LangUsta-KPSS-LoRA | Okul Öncesi Öğretmenliği | 21 | 100 | 21.00% |
| LangUsta-KPSS-LoRA | Parakende Satış ve Mağaza Yöneticiliği | 16 | 100 | 16.00% |
| LangUsta-KPSS-LoRA | Radyo ve Televizyon Programcılığı | 19 | 100 | 19.00% |
| LangUsta-KPSS-LoRA | Sağlık Kurumları İşletmeciliği | 27 | 100 | 27.00% |
| LangUsta-KPSS-LoRA | Sağlık Yönetimi | 16 | 100 | 16.00% |
| LangUsta-KPSS-LoRA | Siyer | 17 | 100 | 17.00% |
| LangUsta-KPSS-LoRA | Sosyal Hizmet | 19 | 100 | 19.00% |
| LangUsta-KPSS-LoRA | Sosyal Hizmetler | 23 | 100 | 23.00% |
| LangUsta-KPSS-LoRA | Sosyoloji | 15 | 100 | 15.00% |
| LangUsta-KPSS-LoRA | Spor Yönetimi | 19 | 100 | 19.00% |
| LangUsta-KPSS-LoRA | TUS | 19 | 100 | 19.00% |
| LangUsta-KPSS-LoRA | Tarih | 21 | 100 | 21.00% |
| LangUsta-KPSS-LoRA | Tarım | 16 | 100 | 16.00% |
| LangUsta-KPSS-LoRA | Turizm ve Otel İşletmeciliği | 24 | 100 | 24.00% |
| LangUsta-KPSS-LoRA | Turizm ve Seyehat Hizmetleri | 22 | 100 | 22.00% |
| LangUsta-KPSS-LoRA | Türk Dili ve Edebiyatı | 30 | 100 | 30.00% |
| LangUsta-KPSS-LoRA | Tıbbi Dökümantasyon ve Sekreterlik | 20 | 100 | 20.00% |
| LangUsta-KPSS-LoRA | Uluslar Arası İlişkiler | 29 | 100 | 29.00% |
| LangUsta-KPSS-LoRA | Uluslararası Ticaret ve Lojistik Yönetimi | 18 | 100 | 18.00% |
| LangUsta-KPSS-LoRA | Yaşlı Bakımı | 17 | 100 | 17.00% |
| LangUsta-KPSS-LoRA | Yerel Yönetimler | 25 | 100 | 25.00% |
| LangUsta-KPSS-LoRA | Yönetim Bİlişim Sistemleri | 18 | 100 | 18.00% |
| LangUsta-KPSS-LoRA | Çalışma Ekonomisi ve Endüstri İlişkileri | 26 | 100 | 26.00% |
| LangUsta-KPSS-LoRA | Çağrı Merkezi Hizmetleri | 20 | 100 | 20.00% |
| LangUsta-KPSS-LoRA | Çocuk Gelişimi | 26 | 100 | 26.00% |
| LangUsta-KPSS-LoRA | Özel Koruma ve Güvenlik | 16 | 100 | 16.00% |
| LangUsta-KPSS-LoRA | Üniversite Giriş Sınavı Temel Bilimler | 20 | 100 | 20.00% |
| LangUsta-KPSS-LoRA | İktisat | 24 | 100 | 24.00% |
| LangUsta-KPSS-LoRA | İlahiyat | 17 | 100 | 17.00% |
| LangUsta-KPSS-LoRA | İnsan Kaynakları Yönetimi | 20 | 100 | 20.00% |
| LangUsta-KPSS-LoRA | İşletme Yönetimi | 22 | 100 | 22.00% |

## Reproduction

```bash
uv sync --python 3.12
uv run python olcum.py
```

> This file is generated automatically by `olcum.py`.
