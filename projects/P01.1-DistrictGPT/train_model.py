"""
Mini transformer modeli eğitimi — BPE tokenizer + Qwen3 mimarisi.

Kullanım:
    python3 train_model.py

Eğitim sonrası:
    - model_checkpoint.pt  (ağırlıklar + tokenizer + config)
    - Örnek metin üretimi ekrana basılır
"""

import os
import sys

import torch

# Model dosyalarının yolu
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "model_files"))

from config import ModelConfig
from model import TinyQwen
from bpe_tokenizer import BPETokenizer

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Hyperparametreler
# ---------------------------------------------------------------------------
DATA_FILE = os.path.join(PROJECT_DIR, "data", "text.txt")
CHECKPOINT_FILE = os.path.join(PROJECT_DIR, "model_checkpoint.pt")
VOCAB_SIZE = 200          # BPE hedef vocab büyüklüğü
BATCH_SIZE = 32
BLOCK_SIZE = 32           # eğitimde kullanılan pencere (token cinsinden)
STEPS = 5000
LEARNING_RATE = 3e-3
EVAL_EVERY = 500
SEED = 1337

device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(SEED)
print(f"Kullanılan cihaz: {device}")

# ---------------------------------------------------------------------------
# 1) BPE Tokenizer'ı eğit
# ---------------------------------------------------------------------------
print(f"\n[1] BPE tokenizer eğitiliyor... (target_vocab_size={VOCAB_SIZE})")
tokenizer = BPETokenizer(target_vocab_size=VOCAB_SIZE)
with open(DATA_FILE, "r", encoding="utf-8") as f:
    raw_text = f.read()
tokenizer.train(raw_text)
print(f"    Vocab büyüklüğü: {tokenizer.vocab_size}")
print(f"    Merge kuralı: {len(tokenizer.merges)}")
print(f"    EOS ID (\\n): {tokenizer.eos_id}")

# ---------------------------------------------------------------------------
# 2) Tüm veriyi encode et — düz ID dizisi
# ---------------------------------------------------------------------------
print("\n[2] Veri encode ediliyor...")
data = torch.tensor(tokenizer.encode(raw_text), dtype=torch.long)
print(f"    Karakter: {len(raw_text):,} → Token: {len(data):,} "
      f"(%{100 - 100*len(data)/len(raw_text):.0f} sıkıştırma)")


def get_batch():
    """Rastgele BATCH_SIZE tane pencere örnekle."""
    ix = torch.randint(len(data) - BLOCK_SIZE - 1, (BATCH_SIZE,))
    x = torch.stack([data[i:i + BLOCK_SIZE] for i in ix])
    y = torch.stack([data[i + 1:i + 1 + BLOCK_SIZE] for i in ix])
    return x.to(device), y.to(device)


# ---------------------------------------------------------------------------
# 3) Modeli oluştur
# ---------------------------------------------------------------------------
print("\n[3] Model oluşturuluyor...")
cfg = ModelConfig(
    vocab_size=tokenizer.vocab_size,
    hidden_size=64,          # biraz büyüttük (32 → 64)
    num_layers=3,            # 2 → 3 katman
    num_heads=4,
    num_kv_heads=2,
    head_dim=16,             # 64 / 4 = 16
    intermediate_size=128,   # ~2x hidden_size
    max_seq_len=256,         # paragraflar için yeterli
    rope_theta=10000.0,
    rms_norm_eps=1e-6,
)

model = TinyQwen(cfg).to(device)
n_params = sum(p.numel() for p in model.parameters())
print(f"    Parametre: {n_params:,}")
print(f"    Katman: {cfg.num_layers}, Hidden: {cfg.hidden_size}, "
      f"Head: {cfg.num_heads}, SeqLen: {cfg.max_seq_len}")

optimizer = torch.optim.AdamW(model.parameters(), lr=LEARNING_RATE)


# ---------------------------------------------------------------------------
# 4) Örnek üretme fonksiyonu
# ---------------------------------------------------------------------------
def generate_text(max_tokens=100, temperature=0.8):
    """\\n'den başla, \\n'ye gelince dur."""
    model.eval()
    with torch.no_grad():
        # Başlangıç: sadece \n token'ı
        start = torch.full((1, 1), tokenizer.eos_id, dtype=torch.long, device=device)
        out = model.generate(
            start,
            max_new_tokens=max_tokens,
            temperature=temperature,
            eos_id=tokenizer.eos_id,
        )
    model.train()
    # Baştaki \n'i at, kalanı decode et
    text = tokenizer.decode(out[0].tolist()[1:])
    # \n'lerden temizle, ilk paragrafı al
    return text.replace("\n", " ").strip()


# ---------------------------------------------------------------------------
# 5) Eğitim döngüsü
# ---------------------------------------------------------------------------
print("\n[4] Eğitim başlıyor...\n")
print(f"{'Adım':>6}  {'Loss':>8}  {'Örnek üretim':<50}")
print("-" * 70)

for step in range(1, STEPS + 1):
    x, y = get_batch()
    _, loss = model(x, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if step % EVAL_EVERY == 0 or step == 1 or step == STEPS:
        sample = generate_text(max_tokens=60, temperature=0.8)
        print(f"{step:6d}  {loss.item():.4f}  {sample[:50]}")

# ---------------------------------------------------------------------------
# 6) Modeli kaydet
# ---------------------------------------------------------------------------
print(f"\n[5] Model kaydediliyor...")
checkpoint = {
    "model": model.state_dict(),
    "cfg": cfg,
    "tokenizer_chars": None,  # BPE kendi vocab'ını taşır
    "tokenizer_merges": tokenizer.merges,
    "tokenizer_vocab": tokenizer.token_to_id,
    "tokenizer_eos_id": tokenizer.eos_id,
}
torch.save(checkpoint, CHECKPOINT_FILE)
print(f"    {CHECKPOINT_FILE} → kaydedildi")

# ---------------------------------------------------------------------------
# 7) Son üretim
# ---------------------------------------------------------------------------
print("\n[6] Örnek üretimler (temperature=0.8):")
for i in range(5):
    text = generate_text(max_tokens=80, temperature=0.8)
    print(f"  {i+1}. {text[:80]}")

print("\nTamamlandı!")
