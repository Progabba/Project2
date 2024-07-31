import json
from abc import ABC, abstractmethod
from typing import List
from .vacancy import Vacancy

class VacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> List[Vacancy]:
        pass

class JSONSaver(VacancySaver):
    def __init__(self, filename: str = "data/vacancies.json"):
        self.filename = filename

    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        vacancies.append(vacancy)
        self._save_to_file(vacancies)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v != vacancy]
        self._save_to_file(vacancies)

    def get_vacancies(self) -> List[Vacancy]:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return [Vacancy(**vac) for vac in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_to_file(self, vacancies: List[Vacancy]) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([vac.__dict__ for vac in vacancies], file, ensure_ascii=False, indent=4)
