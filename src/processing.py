from typing import List, Dict


def filter_by_state(list_dict: list[Dict], value_key: str = "EXECUTED") -> list[Dict]:
    """Функуия, которая возвращает новый список словарей по указанному ключу"""
    new_list_dict = []
    for every_dict in list_dict:
       if every_dict["state"] == value_key:
           new_list_dict.append(every_dict)
    return new_list_dict


def sort_by_date(list_dict: list[Dict], arg_for_sort: bool = True) -> list[Dict]:
    """Функция сортировки списка банковских операций по дате (по умолчанию-убывание)"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict.get("date", ""), reverse=arg_for_sort)
    return sort_list


if __name__ == "__main__":
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
