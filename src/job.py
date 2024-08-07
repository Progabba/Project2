from typing import List, Dict, Any, Optional

class Vacancy:
    """
    Класс для представления вакансии.
    """
    def __init__(self, title: str, url: str, salary_from: Optional[int], salary_to: Optional[int], description: str):
        self.title = title
        self.url = url
        self.salary_from = self._validate_salary(salary_from, 0)
        self.salary_to = self._validate_salary(salary_to, 'не указано')
        self.description = description

    def __str__(self) -> str:
        return f"{self.title} ({self.url}): {self.salary_from} - {self.salary_to} RUB, {self.description}"

    def _validate_salary(self, salary: Optional[int], default: Any) -> Any:
        """
        Приватный метод для валидации зарплаты.
        Возвращает значение зарплаты, если она задана, или значение по умолчанию.
        """
        return salary if salary is not None else default

    @staticmethod
    def cast_to_object_list(vacancies: List[Dict[str, Any]]) -> List['Vacancy']:
        vacancy_objects = []
        for v in vacancies:
            salary = v.get('salary')
            # Если salary не None, то используем метод get для извлечения данных
            salary_from = salary.get('from') if salary is not None else None
            salary_to = salary.get('to') if salary is not None else None

            vacancy_objects.append(
                Vacancy(
                    title=v['name'],
                    url=v['alternate_url'],
                    salary_from=salary_from,
                    salary_to=salary_to,
                    description=v.get('snippet', {}).get('requirement', '')
                )
            )
        return vacancy_objects

    def __lt__(self, other: 'Vacancy') -> bool:
        return self.salary_from < other.salary_from

    def __le__(self, other: 'Vacancy') -> bool:
        return self.salary_from <= other.salary_from

    def __eq__(self, other: 'Vacancy') -> bool:
        return self.salary_from == other.salary_from

    def __ne__(self, other: 'Vacancy') -> bool:
        return self.salary_from != other.salary_from

    def __gt__(self, other: 'Vacancy') -> bool:
        return self.salary_from > other.salary_from

    def __ge__(self, other: 'Vacancy') -> bool:
        return self.salary_from >= other.salary_from

if __name__ == '__main__':
    test_vacancies = [
        {
            'name': 'Python Developer',
            'alternate_url': 'http://example.com',
            'salary': {'from': 100000, 'to': 150000},
            'snippet': {'requirement': 'Опыт работы от 3 лет'}
        },
        {
            'name': 'Senior Python Developer',
            'alternate_url': 'http://example.com',
            'salary': None,  # Нет информации о зарплате
            'snippet': {'requirement': 'Опыт работы от 5 лет'}
        }
    ]

    vacancies = Vacancy.cast_to_object_list(test_vacancies)
    for vacancy in vacancies:
        print(vacancy)

    # Пример использования сравнения
    print(vacancies[0] > vacancies[1])  # Проверка, больше ли зарплата в первой вакансии, чем во второй
