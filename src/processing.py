import typing


def filter_by_state(list_dict: list[typing.Dict], value_key: str = "EXECUTED") -> list[typing.Dict]:
    """Функуия, которая возвращает новый список словарей по указанному ключу"""
    new_list_dict = []
    for every_dict in list_dict:
        if every_dict["state"] == value_key:
            new_list_dict.append(every_dict)
    return new_list_dict


def sort_by_date(list_dict: list[typing.Dict], arg_for_sort: bool = True) -> list[typing.Dict]:
    """Функция сортировки списка банковских операций по дате (по умолчанию-убывание)"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict.get("date", ""), reverse=arg_for_sort)
    return sort_list
