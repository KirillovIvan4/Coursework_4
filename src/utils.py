import json
import requests

def get_list():
    """Функция считывает json файл преобразует его список"""
    with open('./data/vacancies.json', 'r', encoding='utf-8') as json_data_vacancies:
        data_vacancies = json.load(json_data_vacancies)
        return data_vacancies


def upload_and_record_exchange_rates():
    """
    Функция получает курс валют на текущую дату от центробанка
    """
    response = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    result = response.json()['rates']
    return result

