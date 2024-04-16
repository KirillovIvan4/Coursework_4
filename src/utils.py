import json


def get_list():
    """Функция считывает json файл преобразует его список"""
    with open('./data/vacancies.json', 'r', encoding='utf-8') as json_data_vacancies:
        data_vacancies = json.load(json_data_vacancies)
        return data_vacancies
