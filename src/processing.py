def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция, которая фильтрует банковские транзакции на основе их статуса."""
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, сортирующая банковские транзакции по дате."""
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
