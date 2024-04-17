

class FilterVacancies:
    def __init__(self, list_vacancies:list):
        self.list_vacancies = list_vacancies

    # def filter_by_area(self,area):
    #     new_list_vacancies= []
    #     for vacancies in self.list_vacancies:
    #         # if vacancies.area["name"] != area:
    #         #     self.list_vacancies.remove(vacancies)
    #         if vacancies.area["name"] == area:
    #             new_list_vacancies.append(vacancies)
    #
    #     return new_list_vacancies
    def __repr__(self):
        return f"{len(self.list_vacancies)} {self.list_vacancies}"
    @classmethod
    def filter_by_area(cls,list_vacancies, area ):
        new_list_vacancies= []
        for vacancies in list_vacancies:
            if vacancies.area["name"] == area:
                new_list_vacancies.append(vacancies)
        return cls(new_list_vacancies)
