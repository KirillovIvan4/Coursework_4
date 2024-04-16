class Vacancies:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, id, name, area):
        self.id = id
        self.name = name
        self.area = area

    def __repr__(self):
        return f"{self.id } {self.name} {self.area}"


