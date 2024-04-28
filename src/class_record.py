from abc import ABC, abstractmethod


class Record(ABC):


    @abstractmethod
    def record_vacancies(self):
        pass