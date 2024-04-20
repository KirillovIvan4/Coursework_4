

class FilterVacancies:
    def __init__(self, list_vacancies:list):
        self.list_vacancies = list_vacancies


    def __repr__(self):
        return f"{len(self.list_vacancies)} {self.list_vacancies}"

    def __str__(self):
        return f"Найдено вакансий - {FilterVacancies.__len__(self)}"

    def __len__(self):
        len_vacancies = len(self.list_vacancies)
        return len_vacancies
    @classmethod
    def filter_by_area(cls, list_vacancies, area):
        new_list_vacancies= []
        for vacancies in list_vacancies:
            if vacancies.area["name"] == area:
                new_list_vacancies.append(vacancies)
        if len(new_list_vacancies) == 0:
            return f"Такого годода нет"
        else:
            return cls(new_list_vacancies)

    @classmethod
    def filter_by_salary(cls,list_vacancies:list):
        filter_by_salary_vacancies = sorted(list_vacancies, key=lambda x:(x.salary["to"]), reverse=True)
        return cls(filter_by_salary_vacancies)

    @classmethod
    def filter_by_schedule(cls, list_vacancies, schedule):
        new_list_vacancies = []
        for vacancies in list_vacancies:
            if vacancies.schedule["name"] == schedule:
                new_list_vacancies.append(vacancies)

        return cls(new_list_vacancies)

    @classmethod
    def filter_by_experience(cls, list_vacancies, experience):
        new_list_vacancies = []
        for vacancies in list_vacancies:
            if vacancies.experience["name"] == experience:
                new_list_vacancies.append(vacancies)

        return cls(new_list_vacancies)

    @classmethod
    def filter_by_employment(cls, list_vacancies, employment):
        new_list_vacancies = []
        for vacancies in list_vacancies:
            if vacancies.employment["name"] == employment:
                new_list_vacancies.append(vacancies)

        return cls(new_list_vacancies)