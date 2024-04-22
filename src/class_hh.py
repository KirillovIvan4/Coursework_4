from src import class_parser
import requests
import json
class Parser:
    pass

class HH(class_parser.Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        # text - Текст для поиска. Переданное значение ищется в названии и описании работодателя
        # page - Номер страницы с работодателями (считается от 0, по умолчанию — 0)
        # per_page - Количество элементов на страницу (по умолчанию — 20, максимум — 100)
        self.params = {'text': '', 'page': 0, 'per_page': 100}


    def upload_and_record_vacancies(self, keyword, page):
        """
        Метод upload_and_record_vacancies реализует загрузку в файл vacancies.json вакансий
        с ключевым словом "keyword" введеных пользователем. 100 вакансий с первой страници hh.ru
        :param keyword: слово введенное пользователем. По этому слову ищутся вакансии
        :return: возвращается файл vacancies.json
        """

        if keyword == '':
            raise ValueError("Вы не ввели вакансию!")
        vacancies = []

        while self.params.get('page') != 2:
            self.params['text'] = keyword


            response = requests.get(self.url, headers=self.headers, params=self.params)
            result = response.json()["items"]
            for vacancy_number in range(len(result)):
                vacancy = {}
                # id вакансии
                vacancy["id"] = result[vacancy_number]["id"]
                # Название вакансии
                vacancy["name"] = result[vacancy_number]["name"]
                # Место где вакансия
                vacancy["area"] = result[vacancy_number]["area"]
                # Зарплата
                vacancy["salary"] = result[vacancy_number]["salary"]
                # Работадатель
                vacancy["employer"] = result[vacancy_number]["employer"]
                # Описание вакансии
                vacancy["snippet"] = result[vacancy_number]["snippet"]
                # Занятость
                vacancy["schedule"] = result[vacancy_number]["schedule"]
                #  Профессиональные роли
                vacancy["professional_roles"] = result[vacancy_number]["professional_roles"]
                # Необходимый опыт
                vacancy["experience"] = result[vacancy_number]["experience"]
                # Занятость
                vacancy["employment"] = result[vacancy_number]["employment"]
                # Ссылка на выкансию
                vacancy["alternate_url"] = result[vacancy_number]["alternate_url"]

                vacancies.append(vacancy)
            self.params['page']  += 1

        with open("data/vacancies.json", "w", encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

