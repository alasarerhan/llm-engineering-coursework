"""
Eğitilmiş modelden metin üretir.

Kullanım:
    python3 generate.py                    # 5 rastgele örnek
    python3 generate.py "İstanbul"         # prompt ile
    python3 generate.py "Ankara" 0.6       # prompt + sıcaklık
"""

import os
import sys

import torch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "model_files"))
from model import TinyQwen
from bpe_tokenizer import BPETokenizer

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_checkpoint(path=os.path.join(PROJECT_DIR, "model_checkpoint.pt")):
    ckpt = torch.load(path, map_location="cpu", weights_only=False)

    tok = BPETokenizer()
    tok.token_to_id = ckpt["tokenizer_vocab"]
    tok.id_to_token = {v: k for k, v in tok.token_to_id.items()}
    tok.merges = ckpt["tokenizer_merges"]
    tok.eos_id = ckpt["tokenizer_eos_id"]
    tok.newline_id = tok.eos_id
    tok.unk_id = tok.token_to_id[tok.UNK]

    model = TinyQwen(ckpt["cfg"])
    model.load_state_dict(ckpt["model"])
    model.eval()
    return model, tok


def generate(model, tok, prompt="", max_tokens=100, temperature=0.7, top_k=20):
    if prompt:
        prompt_ids = tok.encode(prompt)
        if prompt_ids and prompt_ids[-1] != tok.eos_id:
            prompt_ids.append(tok.eos_id)
        start = torch.tensor([prompt_ids], dtype=torch.long)
    else:
        start = torch.full((1, 1), tok.eos_id, dtype=torch.long)

    with torch.no_grad():
        out = model.generate(start, max_new_tokens=max_tokens,
                             temperature=temperature, top_k=top_k,
                             eos_id=tok.eos_id)
    text = tok.decode(out[0].tolist())
    if text.startswith("\n"):
        text = text[1:]
    return text.replace("\n", " ").strip()


def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else ""
    temperature = float(sys.argv[2]) if len(sys.argv) > 2 else 0.8

    model, tok = load_checkpoint()
    print(f"Model: {sum(p.numel() for p in model.parameters()):,} parametre")

    if prompt:
        text = generate(model, tok, prompt=prompt, temperature=temperature)
        print(f"Üretim: {text}")
    else:
        print(f"5 örnek (temperature={temperature}):")
        for i in range(5):
            text = generate(model, tok, temperature=temperature)
            print(f"  {i+1}. {text[:100]}")


if __name__ == "__main__":
    main()
