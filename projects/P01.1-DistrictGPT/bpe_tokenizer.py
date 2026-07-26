"""BPE (Byte Pair Encoding) tokenizer."""

from collections import Counter


class BPETokenizer:
    """BPE tokenizer: öğren (train) → kodla (encode) → çöz (decode)."""

    UNK = "<unk>"

    def __init__(self, target_vocab_size=100):
        self.target_vocab_size = target_vocab_size
        self.merges: list[tuple[tuple[str, str], str]] = []
        self.token_to_id: dict[str, int] = {}
        self.id_to_token: dict[int, str] = {}
        self.eos_id: int = 0
        self.newline_id: int = 0
        self.unk_id: int = 0

    def train(self, text: str) -> None:
        lines = text.strip().split("\n")
        word_freq = Counter(lines)

        splits: dict[str, list[str]] = {}
        for word in word_freq:
            splits[word] = list(word) + ["</w>"]

        chars: set[str] = set()
        for word in word_freq:
            chars.update(list(word))
        chars.add("</w>")
        chars.add("\n")
        chars.add(self.UNK)

        sorted_chars = sorted(chars, key=lambda c: (0 if c == "\n" else 1, c))
        self.token_to_id = {c: i for i, c in enumerate(sorted_chars)}
        self.eos_id = self.token_to_id["\n"]
        self.newline_id = self.eos_id
        self.unk_id = self.token_to_id[self.UNK]

        base_size = len(self.token_to_id)

        for _ in range(self.target_vocab_size - base_size):
            pair_counts: Counter[tuple[str, str]] = Counter()
            for word, freq in word_freq.items():
                syms = splits[word]
                for i in range(len(syms) - 1):
                    pair_counts[(syms[i], syms[i + 1])] += freq

            if not pair_counts:
                break

            best_pair = max(pair_counts, key=pair_counts.get)
            a, b = best_pair
            new_token = a + b

            self.merges.append((best_pair, new_token))

            if new_token not in self.token_to_id:
                new_id = len(self.token_to_id)
                self.token_to_id[new_token] = new_id

            for word in word_freq:
                syms = splits[word]
                yeni = []
                i = 0
                while i < len(syms):
                    if (i < len(syms) - 1 and syms[i] == a and syms[i + 1] == b):
                        yeni.append(new_token)
                        i += 2
                    else:
                        yeni.append(syms[i])
                        i += 1
                splits[word] = yeni

        self.id_to_token = {v: k for k, v in self.token_to_id.items()}

    def encode(self, text: str) -> list[int]:
        tokens: list[int] = []
        lines = text.split("\n")

        for line in lines:
            if not line:
                continue

            symbols = list(line) + ["</w>"]

            for (a, b), merged in self.merges:
                yeni = []
                i = 0
                while i < len(symbols):
                    if (i < len(symbols) - 1 and
                            symbols[i] == a and symbols[i + 1] == b):
                        yeni.append(merged)
                        i += 2
                    else:
                        yeni.append(symbols[i])
                        i += 1
                symbols = yeni

            for s in symbols:
                if s == "</w>":
                    continue
                if s in self.token_to_id:
                    tokens.append(self.token_to_id[s])
                else:
                    tokens.append(self.unk_id)

            tokens.append(self.eos_id)

        return tokens

    def decode(self, ids: list[int]) -> str:
        result = []
        for tid in ids:
            token = self.id_to_token.get(tid, "�")
            token = token.replace("</w>", "")
            result.append(token)
        return "".join(result)

    @property
    def vocab_size(self) -> int:
        return len(self.token_to_id)
