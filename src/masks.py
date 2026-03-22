def get_mask_card_number(card_number: str) -> str:
    """Kart numarasını maskeler (Örn: 7000 79** **** 6361)"""
    if not card_number:
        return "Номер карты отсутствует"

    # Kart numarasını parçalara ayırıp maskeleme işlemi
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Hesap numarasını maskeler (Örn: **4305)"""
    if not account_number:
        return "Номер счета отсутствует"

    return f"**{account_number[-4:]}"