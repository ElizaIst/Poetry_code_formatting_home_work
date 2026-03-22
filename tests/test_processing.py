import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    """Общий набор данных для использования в тестах."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-10T11:43:11.513356"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226782, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615039933, "state": "CANCELED", "date": "2018-10-14T17:03:44.305197"},
    ]

def test_filter_by_state_executed(sample_data):
    """EXECUTED фильтрация теста в соответствии со статусом."""
    result = filter_by_state(sample_data, "EXECUTED")
    # В списке должно быть не более 2 записей EXECUTED.
    assert len(result) == 2
    assert result[0]["state"] == "EXECUTED"
    assert result[1]["state"] == "EXECUTED"

def test_filter_by_state_canceled(sample_data):
    """Проверка фильтрации на основе статуса «ОТМЕНЕНО»."""
    result = filter_by_state(sample_data, "CANCELED")
    # В списке должно быть только 2 отмененные записи.
    assert len(result) == 2
    assert result[0]["state"] == "CANCELED"

def test_sort_by_date(sample_data):
    """Сортировка по дате (тест)."""
    result = sort_by_date(sample_data)
    # Самую последнюю дату (2019 год) следует указывать первой.
    assert result[0]["date"] == "2019-07-10T11:43:11.513356"