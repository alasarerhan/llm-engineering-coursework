---
base_model: Qwen/Qwen2.5-0.5B-Instruct
library_name: peft
pipeline_tag: text-generation
tags:
- unsloth
- lora
- qlora
- kpss
---

# LangUsta KPSS LoRA Adaptörü

`erhanalsr/langusta-kpss-reasoning` ile Unsloth 4-bit QLoRA kullanılarak
eğitilmiş LoRA adaptörüdür. Bu depo tam model ağırlığı değil, PEFT adaptörü içerir.

Temel model: `Qwen/Qwen2.5-0.5B-Instruct`  
Notebook: `notebooks/LangUsta.ipynb`
