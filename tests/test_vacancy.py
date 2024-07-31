import pytest
import os
from src.vacancy import Vacancy
from src.saver import JSONSaver

@pytest.fixture
def saver():
    return JSONSaver("data/test_vacancies.json")

@pytest.fixture
def vacancy():
    return Vacancy("Test", "url", "100000 руб.", "Описание")

def teardown_function():
    if os.path.exists("data/test_vacancies.json"):
        os.remove("data/test_vacancies.json")

def test_add_vacancy(saver, vacancy):
    saver.add_vacancy(vacancy)
    vacancies = saver.get_vacancies()
    assert vacancy in vacancies

def test_delete_vacancy(saver, vacancy):
    saver.add_vacancy(vacancy)
    saver.delete_vacancy(vacancy)
    vacancies = saver.get_vacancies()
    assert vacancy not in vacancies
