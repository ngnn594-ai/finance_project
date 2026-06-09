import json
from pathlib import Path



BASE_DIR = Path("data")
BASE_DIR.mkdir(exist_ok=True)


FILE = BASE_DIR / "data.json"


def load_data():
    if not FILE.exists():
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
