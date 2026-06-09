import subprocess
import sys
from pathlib import Path

import random
import string


def random_string(length=6):
    return "".join(random.choices(string.ascii_lowercase, k=length))


def test_add_random_100_times():
    for _ in range(100):

        amount = random.uniform(1, 1000)

        result = run(CMD + [
            "add",
            "--amount", str(amount),
            "--category", random_string(),
            "--date", "2026-06-05",
            "--description", random_string(10),
            "--currency", "EUR",
            "--type", random.choice(["expense", "income"])
        ])

        assert result.returncode == 0

CMD = [sys.executable, "zabis.py"]


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


# -----------------------
# ADD
# -----------------------

def test_add_valid():
    result = run(CMD + [
        "add",
        "--amount", "10",
        "--category", "food",
        "--date", "2026-06-05",
        "--description", "coffee",
        "--currency", "EUR",
        "--type", "expense"
    ])

    assert result.returncode == 0


def test_add_invalid_amount():
    result = run(CMD + [
        "add",
        "--amount", "0",
        "--category", "food",
        "--date", "2026-06-05",
        "--description", "coffee",
        "--currency", "EUR",
        "--type", "expense"
    ])

    assert result.returncode != 0
    assert "сумма должна быть больше 0" in result.stdout


def test_add_empty_category():
    result = run(CMD + [
        "add",
        "--amount", "10",
        "--category", "   ",
        "--date", "2026-06-05",
        "--description", "coffee",
        "--currency", "EUR",
        "--type", "expense"
    ])

    assert result.returncode != 0


# -----------------------
# STATS
# -----------------------

def test_stats():
    run(CMD + [
        "add",
        "--amount", "10",
        "--category", "food",
        "--date", "2026-06-05",
        "--description", "coffee",
        "--currency", "EUR",
        "--type", "expense"
    ])

    result = run(CMD + ["stats"])

    assert result.returncode == 0
    assert "Всего:" in result.stdout
    assert "Операций:" in result.stdout


# -----------------------
# LIST
# -----------------------

def test_list():
    result = run(CMD + ["list"])

    assert result.returncode == 0
    assert isinstance(result.stdout, str)


# -----------------------
# IMPORT CSV
# -----------------------

def test_import_csv(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text("10,food\n20,transport")

    result = run(CMD + [
        "import_csv",
        "--path", str(file)
    ])

    assert result.returncode == 0


# -----------------------
# EXPORT CSV
# -----------------------

def test_export_csv():
    run(CMD + [
        "add",
        "--amount", "10",
        "--category", "food",
        "--date", "2026-06-05",
        "--description", "coffee",
        "--currency", "EUR",
        "--type", "expense"
    ])

    result = run(CMD + ["export_csv"])

    assert result.returncode == 0