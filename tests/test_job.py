import pytest
from src.job import Vacancy

def test_job_comparison():
    job1 = Vacancy("Job 1", "http://example.com", 1000, 2000, "Description 1")
    job2 = Vacancy("Job 2", "http://example.com", 2000, 3000, "Description 2")
    assert job1 < job2
    assert job2 > job1

def test_cast_to_object_list():
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
            'salary': None,
            'snippet': {'requirement': 'Опыт работы от 5 лет'}
        }
    ]

    vacancies = Vacancy.cast_to_object_list(test_vacancies)
    assert len(vacancies) == 2
    assert vacancies[0].title == 'Python Developer'
    assert vacancies[1].title == 'Senior Python Developer'
    assert vacancies[1].salary_from == 0  # Значение по умолчанию для отсутствующей зарплаты

if __name__ == '__main__':
    pytest.main()
