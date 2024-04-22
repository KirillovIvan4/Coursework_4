import json
import requests

def get_list():
    """
    Функция считывает json файл преобразует его список
    """
    with open('./data/vacancies.json', 'r', encoding='utf-8') as json_data_vacancies:
        data_vacancies = json.load(json_data_vacancies)
        return data_vacancies



def upload_exchange_rates():
    """
    Функция получает курс валют на текущую дату от центробанка
    """
    response = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    result = response.json()['rates']
    return result

def record_exchange_rates():
    """
    Функция сохраняет курс валют в файл
    """
    exchange_rates = upload_exchange_rates()
    with open("data/exchange_rates.json", "w", encoding='utf-8') as file:
        json.dump(exchange_rates, file, ensure_ascii=False, indent=4)



def get_dict_exchange_rates():
    """
    Функция считывает json файл c курсом валют и преобразует его список
    """

    with open('data/exchange_rates.json', 'r', encoding='utf-8') as json_exchange_rates:
        exchange_rates = json.load(json_exchange_rates)
        return exchange_rates

def save_vacancies(list_vacancies):
    """
    Функция сохраняет json файл с отфильтрованными вакансиями
    """
    save_vacancies = []
    for vacancies in list_vacancies:
        save_vacancies.append({
                                    "id":vacancies.id,
                                    "name":vacancies.name,
                                    "area":vacancies.area,
                                    "salary":vacancies.salary,
                                    "employer":vacancies.employer,
                                    "snippet":vacancies.snippet,
                                    "schedule":vacancies.schedule,
                                    "professional_roles":vacancies.professional_roles,
                                    "experience":vacancies.experience,
                                    "employment":vacancies.employment,
                                    "alternate_url":vacancies.alternate_url
                                    },)

    with open("data/save_vacancies.json", "w", encoding="utf-8") as file:
        json.dump(save_vacancies, file, ensure_ascii=False, indent=4)

    return f"Файл записан"

def upload_save_vacancies():
    """
    Функция считывает json файл с сохраненными вакансиями преобразует его список
    """
    with open('data/save_vacancies.json', 'r', encoding='utf-8') as json_save_vacancies:
        save_vacancies = json.load(json_save_vacancies)
        return save_vacancies
