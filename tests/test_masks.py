import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("3587961263747950", "3587 96** **** 7950"),
        ("2200347689732951", "2200 34** **** 2951"),
    ],
)
def test_get_mask_card_number(card_num: str, expected: str) -> None:
    """Тестирование функции, кторая маскирует номер карты"""
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize(
    "acc_num, expected",
    [
        ("56748475120045830019", "**0019"),
        ("91254928640295415522", "**5522"),
        ("83741985278499871324", "**1324"),
        ("1873658400751253170400", "**0400"),
    ],
)
def test_get_mask_account(acc_num: str, expected: str) -> None:
    """Тестирование функции, которая маскирует номер счета"""
    assert get_mask_account(acc_num) == expected
