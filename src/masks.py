from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Принимает на вход номер карты в формате - 7000792289606361,
    и возвращает ее маску 7000 79** **** 6361."""

    return card_number[:4] + " " + card_number[4:6] + "**" + " **** " + card_number[12:16]


def get_mask_account(bank_account_number: Union[str]) -> Union[str]:
    """Принимает на вход номер счета в формате- 73654108430135874305 и
    возвращает его маску **4305."""

    return "**" + bank_account_number[-4:]


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
