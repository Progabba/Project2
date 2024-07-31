from typing import List, Dict, Any


class Vacancy:
    def __init__(self, title: str, url: str, salary: str, description: str):
        self.title = title
        self.url = url
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description if description else ""

    def __lt__(self, other):
        return self._get_salary_value() < other._get_salary_value()

    def __eq__(self, other):
        return self._get_salary_value() == other._get_salary_value()

    def _get_salary_value(self) -> int:
        if self.salary == "Зарплата не указана":
            return 0
        try:
            return int(self.salary.split()[0].replace("-", "").replace(" ", "").replace("руб.", ""))
        except:
            return 0

    @classmethod
    def cast_to_object_list(cls, vacancies_json: List[Dict[str, Any]]) -> List['Vacancy']:
        return [cls(vacancy["name"], vacancy["alternate_url"], vacancy["salary"]["from"] if vacancy["salary"] else None,
                    vacancy["snippet"]["requirement"]) for vacancy in vacancies_json]

    def __repr__(self):
        return f"Vacancy({self.title}, {self.url}, {self.salary}, {self.description})"
