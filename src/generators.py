def filter_by_currency(transactions, currency):
    """
    Функция возвращает итератор,
    который фильтрует транзакции
    на основе конкретной валюты.
    """
    for transaction in transactions:
        # Надежно проверьте код валюты.
        amount_info = transaction.get("operationAmount", {})
        currency_info = amount_info.get("currency", {})
        if currency_info.get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который последовательно возвращает
    описание каждой операции из списка операций.
    """
    for transaction in transactions:
        yield transaction.get("description", "Açıklama yok")


def card_number_generator(start, stop):
    """
    Программа генерирует номера карт
    в формате XXXX XXXX XXXX XXXX в пределах указанного диапазона.
    """
    for number in range(start, stop + 1):
        # Число должно быть 16-значным (слева заполните нулями).
        card_str = f"{number:016d}"
        # Разделив их на группы по четыре человека, используя следующий формат.
        formatted_card = (
            f"{card_str[:4]} {card_str[4:8]} "
            f"{card_str[8:12]} {card_str[12:]}"
        )
        yield formatted_card
