import csv
import pandas as pd
import logging

logger = logging.getLogger('read_csv_excel')
file_hendler = logging.FileHandler('logs/read_csv_excel.log', 'w')
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_hendler.setFormatter(file_formater)
logger.addHandler(file_hendler)
logger.setLevel(logging.DEBUG)


def read_csv_file(file_path: str) -> list:
    """Получение списка транзакции из CSV-файла"""
    logger.info(f"Запрос на чтение CSV-файла {file_path}")
    try:
        transaction_df = pd.read_csv(file_path, delimiter=';')
        result = transaction_df.to_dict(orient='records')
        logger.info("Список транзакций успешно создан")
        return result
    except FileNotFoundError:
        logger.error("Ошибка!Файл не найден!")
        return []
    except Exception as e:
        logger.info(f"Произошла ошибка {e}")
        return []


def read_excel_file(file_path: str) -> list:
    """Получение списка транзакции из EXCEL-файла"""
    logger.info(f"Запрос на чтение EXCEL файла {file_path}")
    try:
        transaction_df = pd.read_excel(file_path)
        result = transaction_df.to_dict(orient='records')
        logger.info("Список транзакций успешно создан")
        return result
    except FileNotFoundError:
        logger.error("Ошибка!Файл не найден!")
        return []
    except Exception as e:
        logger.info(f"Произошла ошибка {e}")
        return []


print(read_csv_file('data/transactions.csv'))
print(read_excel_file('data/transactions_excel.xlsx'))
