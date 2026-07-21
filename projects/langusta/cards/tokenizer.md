---
language:
- en
library_name: transformers
tags:
- tokenizer
- bpe
- kpss
---

# LangUsta Byte-Level BPE Tokenizer

Filtrelenmiş Türkçe KPSS akıl yürütme korpusu üzerinde eğitilmiş 8.000 hedef
vocab boyutlu byte-level BPE tokenizer'dır. `<unk>`, `<pad>`, `<bos>` ve `<eos>` özel tokenlarını içerir.

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("erhanalsr/langusta-kpss-bpe-tokenizer")
ids = tokenizer.encode("KPSS sorusunu gerekçeli çöz.")
print(tokenizer.decode(ids))
```

Bu tokenizer bağımsız ödev çıktısıdır; Qwen LoRA eğitiminde temel modelin kendi tokenizer'ı kullanılmıştır.
