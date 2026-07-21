# Turkish District LM

Türkiye ilçeleri hakkındaki metinler üzerinde özel bir BPE tokenizer ve küçük bir decoder-only Transformer eğiten, eğitim amaçlı sıfırdan dil modeli projesidir.

## Proje Özeti

| Bileşen | Değer |
| --- | --- |
| Görev | Nedensel dil modelleme |
| Veri | Türkiye ilçeleri hakkında Türkçe metin |
| Tokenizer | Proje içinde geliştirilen BPE |
| Mimari | Qwen3 bileşenlerinden uyarlanan küçük decoder-only Transformer |
| Model boyutu | Yaklaşık 124 bin parametre |
| Bağımlılık | PyTorch |

Model; RMSNorm, rotary positional embedding, grouped-query attention ve SwiGLU bileşenlerini kullanan üç Transformer bloğundan oluşur. Küçük boyutu nedeniyle mimariyi incelemek ve eğitim döngüsünü yerel ortamda çalıştırmak için tasarlanmıştır.

## Proje Yapısı

```text
turkish-district-lm/
├── data/text.txt          # Eğitim metni
├── model_files/           # Transformer mimarisi
├── bpe_tokenizer.py       # BPE train/encode/decode
├── train_model.py         # Eğitim ve checkpoint üretimi
├── generate.py            # Checkpoint üzerinden inference
└── requirements.txt
```

## Kurulum

```bash
cd projects/turkish-district-lm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Eğitim

```bash
python3 train_model.py
```

Eğitim tamamlandığında `model_checkpoint.pt` proje klasöründe oluşturulur. Checkpoint tekrar üretilebildiği için Git deposuna dahil edilmez.

## Metin Üretimi

```bash
python3 generate.py
python3 generate.py "İstanbul ilçeleri"
python3 generate.py "Ankara" 0.6
```

## Teknik Notlar

- Tokenizer hedef kelime dağarcığı 200 tokendır.
- Eğitim deterministik başlangıç için `1337` seed değerini kullanır.
- Eğitim cihazı CUDA kullanılabiliyorsa GPU, aksi durumda CPU olarak seçilir.
- Mimari dosyaları kurs kapsamında sağlanan Qwen3 başlangıç kodundan uyarlanmıştır; tokenizer, eğitim akışı ve inference entegrasyonu ödev kapsamında hazırlanmıştır.

## Veri

Eğitim metni Türkiye ilçelerine ilişkin Wikipedia kaynaklı içerikten hazırlanmıştır. Bu küçük veri yalnızca eğitim ve mimari denemeleri amacıyla kullanılmaktadır.
