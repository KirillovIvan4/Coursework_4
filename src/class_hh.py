from src import class_upload, class_record
import requests
import json
class Parser:
    pass

class HH(class_upload.Upload, class_record.Record):
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

    def upload_vacancies(self):
        """
              Метод upload_vacancies реализует загрузку вакансий
              с ключевым словом "keyword" введеных пользователем. 100 вакансий с первой страници hh.ru
              """
        response = requests.get(self.url, headers=self.headers, params=self.params)
        result = response.json()["items"]
        return result

    def record_vacancies(self, keyword, page):
        """
        Метод record_vacancies реализует загрузку в файл vacancies.json вакансий
        с ключевым словом "keyword" введеных пользователем. 100 вакансий с первой страници hh.ru
        :param keyword: слово введенное пользователем. По этому слову ищутся вакансии
        :return: возвращается файл vacancies.json
        """

        if keyword == '':
            raise ValueError("Вы не ввели вакансию!")
        vacancies = []

        while self.params.get('page') != page:
            self.params['text'] = keyword
            result = self.upload_vacancies()
            for vacancy_number in range(len(result)):
                vacancy = {}
                for item in ["id", "name", "area", "salary", "employer", "snippet", "schedule", "professional_roles", "experience", "employment", "alternate_url"]:
                    vacancy[item] = result[vacancy_number][item]
                vacancies.append(vacancy)
            self.params['page']  += 1

        with open("data/vacancies.json", "w", encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

