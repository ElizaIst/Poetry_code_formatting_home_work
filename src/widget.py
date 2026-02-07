from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Программа извлекает и маскирует информацию о карте или счете пользователя.
    Формат ввода: 'Visa Platinum 7000792289606361'
    """
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower().startswith("счет"):
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат 'ДД.ММ.ГГГГ'.
    Пример: '2024-03-11T02:26:18.671407' -> '11.03.2024'
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


