from src import  class_record, class_hh
import requests
import json

class SaveVacancies(class_record.Record):
    def __init__(self, keyword, page):
        self.keyword = keyword
        self.page = page

    def record_vacancies(self):
        """
        Метод record_vacancies реализует загрузку в файл vacancies.json вакансий
        с ключевым словом "keyword" введеных пользователем. 100 вакансий с первой страници hh.ru
        :param keyword: слово введенное пользователем. По этому слову ищутся вакансии
        :return: возвращается файл vacancies.json
        """

        if self.keyword == '':
            raise ValueError("Вы не ввели вакансию!")
        vacancies = []

        params_page = self.page
        params_text = self.keyword
        hh = class_hh.HH(params_text, params_page)
        result = hh.upload_vacancies()
        for vacancy_number in range(len(result)):
            vacancy = {}
            for item in ["id", "name", "area", "salary", "employer", "snippet", "schedule", "professional_roles",
                         "experience", "employment", "alternate_url"]:
                vacancy[item] = result[vacancy_number][item]
            vacancies.append(vacancy)
        params_page += 1



        with open("data/vacancies.json", "w", encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)