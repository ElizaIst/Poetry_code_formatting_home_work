def get_mask_card_number(card_number: int) -> str:
    """Функция, которая маскирует номер карты в формате XXXX XX** **** XXXX """
    str_card = str(card_number)
    return f"{str_card[:4]} {str_card[4:6]}** **** {str_card[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция, которая маскирует номер счета в формате **XXXX """
    str_account = str(account_number)
    return f"**{str_account[-4:]}"
