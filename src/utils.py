from typing import List
from .vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    return [vacancy for vacancy in vacancies if
            vacancy.description and any(keyword.lower() in vacancy.description.lower() for keyword in keywords)]


def get_vacancies_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
    try:
        min_salary, max_salary = map(int, salary_range.split("-"))
    except ValueError:
        raise ValueError("Диапазон зарплат должен быть в формате 'min-max'")

    return [vacancy for vacancy in vacancies if min_salary <= vacancy._get_salary_value() <= max_salary]


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    return sorted(vacancies, reverse=True)[:top_n]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    for vacancy in vacancies:
        print(vacancy)
