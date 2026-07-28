# LangUsta Custom Benchmark Results

The benchmark contains 100 Turkish five-choice questions held out before fine-tuning.
All systems use greedy decoding and strict first-letter exact-match scoring.

| Model | Correct | Accuracy | Valid letter format | Runtime (s) |
|---|---:|---:|---:|---:|
| Qwen2.5-1.5B-Instruct | 33/100 | 33% | 100% | 20.90 |
| LangUsta-MCQ-Letter-LoRA | 29/100 | 29% | 100% | 21.29 |
| SmolLM2-1.7B-Instruct | 23/100 | 23% | 95% | 29.29 |
| Qwen2.5-0.5B-Instruct | 19/100 | 19% | 97% | 22.40 |
| Gemma-3-1B-Instruct-4bit | 19/100 | 19% | 99% | 30.35 |
| TinyLlama-1.1B-Chat | 0/100 | 0% | 1% | 25.09 |
