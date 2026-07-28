# P02.1 - Turkish MMLU Benchmark

This project compares the LangUsta KPSS LoRA adapter against its base model on
the Turkish MMLU benchmark.

## Evaluation Protocol

- Benchmark: TR-MMLU from `malibayram/llm-tr-benchmarks`
- Evaluated questions: 6,200
- Models: `Qwen/Qwen2.5-0.5B-Instruct` and `LangUsta-KPSS-LoRA`
- Decoding: deterministic greedy generation
- Scoring: exact option matching with semantic fallback

## Results

| Model | Correct | Questions | Accuracy |
| --- | ---: | ---: | ---: |
| Qwen2.5-0.5B-Instruct | 1,767 | 6,200 | 28.50% |
| LangUsta-KPSS-LoRA | 1,258 | 6,200 | 20.29% |

Detailed section-level results are available in `results/benchmark-results.md`.

## Reproduction

```bash
uv sync --python 3.12
uv run python olcum.py
```
