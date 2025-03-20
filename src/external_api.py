import os
from dotenv import load_dotenv
import requests


load_dotenv()  # Загружаем переменные окружения из .env файла


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли.

    Args:
        transaction (dict): Словарь с данными о транзакции, содержащий
                           'amount' и 'currency'.
    Returns:
        float: Сумма транзакции в рублях.
    """
    amount = transaction["operationAmount"]["amount"]  # Получаем сумму тразакции
    currency = transaction["operationAmount"]["currency"]["code"]  # Получаем валюту транзакции

    if currency == 'RUB':
        return float(transaction["operationAmount"]["amount"])  # Если валюта уже в рублях, возвращаем сумму

    # Формируем URL для API, чтобы конвертировать валюту
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {
        "apikey": os.getenv("API_KEY")  # Получаем API ключ из переменных окружения
    }

    responce = requests.get(url, headers=headers)  # Запрос к API

    if responce.status_code == 200:  # Если запрос успешен
        return float(responce.json()['result'])  # Возвращаем результат конвертации
    else:
        return float(amount)  # Если API не сработал, возвращаем сумму без изминений
