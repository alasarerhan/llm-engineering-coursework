from langusta.train_tokenizer import SPECIAL_TOKENS, train_bpe, verify_roundtrip


def test_bpe_roundtrip_and_special_tokens(tmp_path):
    corpus = tmp_path / "corpus.txt"
    corpus.write_text(
        ("KPSS sorularını Türkçe ve gerekçeli biçimde çözüyorum.\n"
         "agent = create_agent(model=model, tools=tools)\n"
         "İ, ı, Ş, ş, Ğ, ğ, Ü, ü, Ö, ö, Ç, ç\n") * 10,
        encoding="utf-8",
    )
    tokenizer = train_bpe(corpus, tmp_path / "tokenizer", vocab_size=400)
    verify_roundtrip(tokenizer)
    assert all(token in tokenizer.get_vocab() for token in SPECIAL_TOKENS)
