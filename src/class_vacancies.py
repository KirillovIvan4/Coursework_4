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
        return f"id - {self.id} salary- {self.salary['currency']} "

    def __str__(self):
        return f"""------------------------------
id вакансии - {self.id}
{self.name}
Город - {self.area['name']}
Зарплата в рублях
от - {self.salary["from"]}
до - {self.salary["to"]}
Работодатель - {self.employer['name']}
Обязанности - {self.snippet['requirement']}
График работы - {self.schedule['name']}
Должность -{self.professional_roles[0]['name']}
Опыт -  {self.experience['name']}
Занятость - {self.employment['name']}
Ссылка на вакансию - {self.alternate_url}
------------------------------
"""

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

    def convert_currency_salary(self, exchange_rates):
        exchange_rates = exchange_rates
        if self.salary['currency'] != 'RUR':
            # Замена кода валюты у беларуских рублей на код соответствующий коду у центробанка
            if self.salary['currency'] == 'BYR':
                self.salary['currency'] = "BYN"
            if self.salary['currency'] != 'RUR':
                for currency in exchange_rates:
                    if currency == self.salary['currency']:
                        self.salary["to"] = int(self.salary["to"] / exchange_rates[currency])
                        self.salary["from"] = int(self.salary["from"] / exchange_rates[currency])
                        self.salary['currency'] = 'RUR'

