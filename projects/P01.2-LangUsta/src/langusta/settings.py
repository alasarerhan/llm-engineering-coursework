"""Proje genelindeki sabitler."""

SOURCE_DATASET = "AhmetSemih/Deepseek-mcq-reasoning-dataset"
REFERENCE_DATASET = "alibayram/identity_finetune_magibu_q3"

HF_OWNER = "erhanalsr"
MAIN_DATASET_REPO = f"{HF_OWNER}/langusta-kpss-reasoning"
TOKENIZER_REPO = f"{HF_OWNER}/langusta-kpss-bpe-tokenizer"
MAIN_ADAPTER_REPO = f"{HF_OWNER}/langusta-kpss-lora"
IDENTITY_DATASET_REPO = f"{HF_OWNER}/langusta-identity"
IDENTITY_ADAPTER_REPO = f"{HF_OWNER}/langusta-identity-lora"

BASE_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"
SYSTEM_PROMPT = (
    "Sen KPSS sorularını Türkçe, doğru ve gerekçeli biçimde yanıtlayan bir eğitim asistanısın."
)
IDENTITY_SYSTEM_PROMPT = (
    "Sen LangUsta adlı, Erhan Alasar tarafından oluşturulan Türkçe KPSS eğitim destek asistanısın. "
    "Kısa, doğru ve anlaşılır cevaplar verirsin."
)
