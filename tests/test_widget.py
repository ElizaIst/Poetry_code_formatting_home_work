import pytest
from src.widget import mask_account_card, get_date

# 1. Тест формата даты
def test_get_date():
    """Эта проверка проверяет правильность преобразования формата даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2018-12-31T23:59:59.999999") == "31.12.2018"

# 2.Тест маскирования карт и счетов (с параметризацией)
@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837493216302", "Maestro 1596 83** **** 6302"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Mastercard 7158300714675092", "Mastercard 7158 30** **** 5092")
])
def test_mask_account_card(input_str, expected):
    """Он проверяет, правильно ли замаскированы различные типы карт и счетов."""
    assert mask_account_card(input_str) == expected