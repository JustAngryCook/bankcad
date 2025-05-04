from masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> str:
    """функция принимает информацию о карте, либо счете"""
    numbers = ""
    letters = ""
    for i in string:
        if i.isdigit():
            numbers += i
        if i.isalpha():
            letters += i
    if "Счет" in string:
        return (f"{letters} {get_mask_account(numbers)}")
    else:
        return (f"{letters} {get_mask_card_number(numbers)}")


print(mask_account_card("Счет 64686473678894779589"))
