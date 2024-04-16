

class FilterVacancies:
    def __init__(self, list_vacancies:list):
        self.list_vacancies = list_vacancies

    def filter_by_area(self,area):
        for vacancies in self.list_vacancies:
            if vacancies.area != area:
                self.list_vacancies.remove(vacancies)
        return self.list_vacancies
