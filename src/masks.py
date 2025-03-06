from typing import Union
import logging

# Настройка логирования для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# Форматирование логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(messages)s')
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Принимает на вход номер карты в формате - 7000792289606361,
    и возвращает ее маску 7000 79** **** 6361."""

    logger.debug(f"Получение маски для номера карты: {card_number}")

    # Проверяем что номер карты 16 цифр.
    if len(card_number) != 16 or not card_number.isdigit():
        logger.error("Ошибка: Номер карты должен содержать 16 цифр.")
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Создание маски карты
    mask_card = f"{card_number[:6]}******{card_number[-4:]}"
    logger.info(f"Маска карты успешно создана: {mask_card}")
    return mask_card


def get_mask_account(bank_account_number: Union[str]) -> Union[str]:
    """Принимает на вход номер счета в формате- 73654108430135874305 и
    возвращает его маску **4305."""

    logger.debug(f"Получение маски для номера счета: {bank_account_number}")

    # Проверяем что номер счета

    if len(bank_account_number) != 20 or not bank_account_number.isdigit():
        logger.error("Ошибка номер карты должен содержать 20 цифр.")
        raise ValueError("Номер счета должен состоять из 20 цифр.")

    # Создаем маску, видны последние 4 цифры
    mask_account = f"**{bank_account_number[-4:]}"
    logger.info(f"Маска счета успешно создана: {mask_account}")

    return mask_account
