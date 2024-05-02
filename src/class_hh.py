from src import class_upload, class_record
import requests
import json

class HH(class_upload.Upload):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, text, page):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        # text - Текст для поиска. Переданное значение ищется в названии и описании работодателя
        # page - Номер страницы с работодателями (считается от 0, по умолчанию — 0)
        # per_page - Количество элементов на страницу (по умолчанию — 20, максимум — 100)
        self.text = text
        self.page = page

        self.params = {'self.text':self.text, 'page': self.page , 'per_page': 100}

    def upload_vacancies(self):
        """
              Метод upload_vacancies реализует загрузку вакансий
              с ключевым словом "keyword" введеных пользователем. 100 вакансий с первой страници hh.ru
              """
        response = requests.get(self.url, headers=self.headers, params=self.params)
        result = response.json()["items"]
        return result


