from typing import List, Dict, Any, Optional

class Vacancy:
    """
    Класс для представления вакансии.
    """
    def __init__(self, title: str, url: str, salary_from: Optional[int], salary_to: Optional[int], description: str):
        self.title = title
        self.url = url
        self.salary_from = salary_from or 0
        self.salary_to = salary_to or 'не указано'
        self.description = description

    def __str__(self) -> str:
        return f"{self.title} ({self.url}): {self.salary_from} - {self.salary_to} RUB, {self.description}"

    @staticmethod
    def cast_to_object_list(vacancies: List[Dict[str, Any]]) -> List['Vacancy']:
        vacancy_objects = []
        for v in vacancies:
            salary = v.get('salary', {})
            vacancy_objects.append(
                Vacancy(
                    title=v['name'],
                    url=v['alternate_url'],
                    salary_from=salary.get('from') if salary else None,
                    salary_to=salary.get('to') if salary else None,
                    description=v.get('snippet', {}).get('requirement', '')
                )
            )
        return vacancy_objects

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
