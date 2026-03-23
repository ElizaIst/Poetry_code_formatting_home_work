def get_mask_card_number(card_number: str) -> str:
    """Это скрывает номер карты (например, 7000 79** **** 6361)."""
    if not card_number:
        return "Номер карты отсутствует"

    # Процесс детализации и маскировки номера карты.
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Это скрывает номер счета (например, **4305)."""
    if not account_number:
        return "Номер счета отсутствует"

    return f"**{account_number[-4:]}"

