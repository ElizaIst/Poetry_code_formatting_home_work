import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize("card_num, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
    ("", "Номер карты отсутствует")
])
def test_get_mask_card_number(card_num, expected):
    assert get_mask_card_number(card_num) == expected
