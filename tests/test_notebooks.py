import json
import re
from pathlib import Path


def test_colab_notebooks_are_valid_and_do_not_contain_tokens():
    notebooks = [Path("notebooks/LangUsta.ipynb")]
    assert notebooks[0].is_file()
    for path in notebooks:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        assert notebook["nbformat"] == 4
        text = json.dumps(notebook)
        assert "OPENCODE" not in text.upper()
        assert "from openai import" not in text
        assert "userdata.get" not in text
        assert re.search(r"hf_[A-Za-z0-9]{20,}", text) is None
        assert text.count("push_to_hub") == 3
        assert "PUBLISH = False" not in text
        assert "load_dotenv(env_path, override=True)" in text
        assert "RUNTIME_ROOT / '.env'" in text
