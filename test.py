


# ebal ia v rot eti pytesti u unitTesti , krch chat gpt moment

import pytest

from services import get_next_id, filter_transactions
from report import get_stats


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "type": "income",
            "amount": 1000,
            "category": "salary",
            "date": "2026-06-01",
            "comment": "salary"
        },
        {
            "id": 2,
            "type": "expense",
            "amount": 100,
            "category": "food",
            "date": "2026-06-02",
            "comment": "lunch"
        },
        {
            "id": 3,
            "type": "expense",
            "amount": 50,
            "category": "transport",
            "date": "2026-06-03",
            "comment": "bus"
        }
    ]


# --------------------
# get_next_id
# --------------------

def test_get_next_id_empty():
    assert get_next_id([]) == 1


def test_get_next_id_single():
    assert get_next_id([{"id": 1}]) == 2


def test_get_next_id_multiple():
    data = [{"id": 1}, {"id": 5}, {"id": 3}]
    assert get_next_id(data) == 6


# --------------------
# filter_transactions
# --------------------

def test_filter_by_type(monkeypatch, sample_transactions):
    monkeypatch.setattr(
        "services.load_data",
        lambda: sample_transactions
    )

    result = filter_transactions(tx_type="income")

    assert len(result) == 1
    assert result[0]["type"] == "income"


def test_filter_by_category(monkeypatch, sample_transactions):
    monkeypatch.setattr(
        "services.load_data",
        lambda: sample_transactions
    )

    result = filter_transactions(category="food")

    assert len(result) == 1
    assert result[0]["category"] == "food"


def test_filter_start_date(monkeypatch, sample_transactions):
    monkeypatch.setattr(
        "services.load_data",
        lambda: sample_transactions
    )

    result = filter_transactions(start_date="2026-06-02")

    assert len(result) == 2


def test_filter_end_date(monkeypatch, sample_transactions):
    monkeypatch.setattr(
        "services.load_data",
        lambda: sample_transactions
    )

    result = filter_transactions(end_date="2026-06-02")

    assert len(result) == 2


def test_filter_not_found(monkeypatch, sample_transactions):
    monkeypatch.setattr(
        "services.load_data",
        lambda: sample_transactions
    )

    result = filter_transactions(category="crypto")

    assert result == []


def test_filter_without_params(monkeypatch, sample_transactions):
    monkeypatch.setattr(
        "services.load_data",
        lambda: sample_transactions
    )

    result = filter_transactions()

    assert len(result) == 3


# --------------------
# get_stats
# --------------------

def test_stats(monkeypatch, sample_transactions):
    monkeypatch.setattr(
        "report.load_data",
        lambda: sample_transactions
    )

    income, expense = get_stats()

    assert income == 1000
    assert expense == 150


def test_stats_only_income(monkeypatch):
    data = [
        {
            "id": 1,
            "type": "income",
            "amount": 500,
            "category": "salary",
            "date": "2026-06-01",
            "comment": "salary"
        }
    ]

    monkeypatch.setattr(
        "report.load_data",
        lambda: data
    )

    income, expense = get_stats()

    assert income == 500
    assert expense == 0


def test_stats_empty(monkeypatch):
    monkeypatch.setattr(
        "report.load_data",
        lambda: []
    )

    income, expense = get_stats()

    assert income == 0
    assert expense == 0


# --------------------
# structure
# --------------------

def test_transaction_has_required_fields(sample_transactions):
    item = sample_transactions[0]

    assert set(item.keys()) == {
        "id",
        "type",
        "amount",
        "category",
        "date",
        "comment"
    }