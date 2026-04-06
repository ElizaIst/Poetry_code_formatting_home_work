import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def transactions_data():
    return [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transfer A"},
        {"operationAmount": {"currency": {"code": "RUB"}}, "description": "Transfer B"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transfer C"},
    ]

def test_filter_by_currency(transactions_data):
    usd_iter = filter_by_currency(transactions_data, "USD")
    result = list(usd_iter)
    assert len(result) == 2
    assert result[0]["description"] == "Transfer A"

def test_transaction_descriptions(transactions_data):
    descriptions = list(transaction_descriptions(transactions_data))
    assert descriptions == ["Transfer A", "Transfer B", "Transfer C"]

@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, "0000 0000 0000 0001"),
    (10, 10, "0000 0000 0000 0010"),
])
def test_card_number_generator(start, stop, expected):
    gen = card_number_generator(start, stop)
    assert next(gen) == expected
