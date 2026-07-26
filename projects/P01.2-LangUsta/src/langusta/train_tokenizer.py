"""Temiz KPSS korpusu üzerinde Transformers uyumlu byte-level BPE eğitir."""

from __future__ import annotations

import argparse
from pathlib import Path

from tokenizers import Tokenizer
from tokenizers.decoders import ByteLevel as ByteLevelDecoder
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import ByteLevel
from tokenizers.trainers import BpeTrainer
from transformers import AutoTokenizer, PreTrainedTokenizerFast

from .settings import TOKENIZER_REPO

SPECIAL_TOKENS = ["<unk>", "<pad>", "<bos>", "<eos>"]


def train_bpe(corpus_file: Path, output_dir: Path, vocab_size: int = 8_000) -> PreTrainedTokenizerFast:
    if not corpus_file.is_file() or not corpus_file.read_text(encoding="utf-8").strip():
        raise FileNotFoundError(f"Corpus bulunamadı veya boş: {corpus_file}")

    backend = Tokenizer(BPE(unk_token="<unk>"))
    backend.pre_tokenizer = ByteLevel(add_prefix_space=False)
    backend.decoder = ByteLevelDecoder()
    trainer = BpeTrainer(
        vocab_size=vocab_size,
        min_frequency=2,
        special_tokens=SPECIAL_TOKENS,
        initial_alphabet=ByteLevel.alphabet(),
        show_progress=True,
    )
    backend.train([str(corpus_file)], trainer)
    tokenizer = PreTrainedTokenizerFast(
        tokenizer_object=backend,
        unk_token="<unk>",
        pad_token="<pad>",
        bos_token="<bos>",
        eos_token="<eos>",
        model_max_length=2_048,
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    tokenizer.save_pretrained(output_dir)
    return tokenizer


def verify_roundtrip(tokenizer: PreTrainedTokenizerFast) -> None:
    samples = [
        "KPSS sorularını Türkçe ve gerekçeli biçimde çözüyorum.",
        "agent = create_agent(model=model, tools=tools)",
        "İ, ı, Ş, ş, Ğ, ğ, Ü, ü, Ö, ö, Ç, ç",
    ]
    for sample in samples:
        decoded = tokenizer.decode(tokenizer.encode(sample), skip_special_tokens=True)
        if decoded != sample:
            raise AssertionError(f"Round-trip başarısız: {sample!r} != {decoded!r}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=Path, default=Path("artifacts/main_dataset/corpus.txt"))
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/tokenizer"))
    parser.add_argument("--vocab-size", type=int, default=8_000)
    parser.add_argument("--push", action="store_true")
    parser.add_argument("--repo-id", default=TOKENIZER_REPO)
    parser.add_argument("--token", default=None)
    args = parser.parse_args()

    tokenizer = train_bpe(args.corpus, args.output_dir, args.vocab_size)
    verify_roundtrip(tokenizer)
    print(f"Tokenizer hazır: vocab={len(tokenizer)}, konum={args.output_dir}")

    if args.push:
        tokenizer.push_to_hub(args.repo_id, token=args.token, private=False)
        loaded = AutoTokenizer.from_pretrained(args.repo_id, token=args.token)
        verify_roundtrip(loaded)
        print(f"Yüklendi ve doğrulandı: https://huggingface.co/{args.repo_id}")


if __name__ == "__main__":
    main()
