import os
from dotenv import load_dotenv
import requests


load_dotenv()  # Загружаем переменные окружения из .env файла


def convert_to_rub(operationAmount: dict) -> float:
    """Конвертирует сумму транзакции в рубли.

    Args:
        operationAmount (dict): Словарь с данными о транзакции, содержащий
                           'amount' и 'currency'.
    Returns:
        float: Сумма транзакции в рублях.
    """
    amount = operationAmount['amount']  # Получаем сумму тразакции
    currency = operationAmount['currency']  # Получаем валюту транзакции

    if currency == 'RUB':
        return float(amount)  # Если валюта уже в рублях, возвращаем сумму

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
