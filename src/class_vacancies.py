from src import utils
class Vacancies:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, id, name, area, salary, employer, snippet, schedule, professional_roles, experience, employment, alternate_url):
        self.id = id
        self.name = name
        self.area = area
        self.salary = salary
        self.employer = employer
        self.snippet =snippet
        self.schedule = schedule
        self.professional_roles = professional_roles
        self.experience = experience
        self.employment = employment
        self.alternate_url = alternate_url


    def __repr__(self):
        return f"salary- {self.salary['currency']} "


    def editing_salary(self):
        """
        Проверяет наличие from и to в salary, в случаи отсутствия to приравнивается к 0 и добавляет валюту.
        Проверяет наличие to в salary, в случаи отсутствия to приравнивается к from.
        """

        if self.salary == None:
            self.salary  =  {'from': 0, "to":0, 'currency': 'RUR'}
        else:
            if self.salary["to"] == None:
                self.salary["to"] = self.salary["from"]
            if self.salary["from"] == None:
                self.salary["from"] = 0

    def a_salary(self):
        exchange_rates = utils.upload_and_record_exchange_rates()
        if self.salary['currency'] != 'RUR':
             for currency in exchange_rates:
                 if currency == self.salary['currency']:
                     self.salary["to"] = int(self.salary["to"] / exchange_rates[currency])
                     self.salary["from"] = int(self.salary["from"] / exchange_rates[currency])


