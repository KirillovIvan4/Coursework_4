from abc import ABC, abstractmethod
class Upload(ABC):

    @abstractmethod
    def upload_vacancies(self):
        pass