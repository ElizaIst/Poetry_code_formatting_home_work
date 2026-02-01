from src.masks import get_mask_account, get_mask_card_number
def mask_account_card(info: str) -> str:
    """
        Kart veya hesap bilgisini alır ve uygun maskelemeyi döner.
        Örn: 'Visa Platinum 7000792289606361' -> 'Visa Platinum 7000 79** **** 6361'
        """
    parts = info.split(' ')
    number = parts[-1] #Son parca numaradir
    name = " ".join(parts[:-1]) # Geriye kalan her sey isimdir

    if name.lower() == "счет":
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"

def get_date(date_string: str) -> str:
    """ISO formatındaki tarihi 'GG.AA.YYYY' formatına çevirir."""
    date_part = date_string[:10]
    year, month, day = date_part.split("-")
    # Gün ve Yıl yer değiştirmeli
    return f"{day}.{month}.{year}"
