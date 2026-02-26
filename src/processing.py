from typing import List, Dict, Any


def filter_by_state(
        data: List[Dict[str, Any]], state: str = 'EXECUTED'
) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей с данными о банковских операциях.
    :param state: Статус для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только элементы
     с указанным статусом.
    """
    filtered_list = []
    for item in data:
        if item.get('state') == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(
    data: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате (ключ 'date').

    :param data: Список словарей с данными о банковских операциях.
    :param reverse: Порядок сортировки (по умолчанию True — по убыванию).
    :return: Новый список, отсортированный по дате.
    """
    return sorted(
        data,
        key=lambda x: x['date'],
        reverse=reverse
    )
