import pytest
from src.vacancy import Vacancy

def test_salary_comparison():
    vacancy1 = Vacancy("Dev", "url", "50000 руб.", "Описание")
    vacancy2 = Vacancy("Dev", "url", "100000 руб.", "Описание")
    assert vacancy1 < vacancy2
    assert not (vacancy1 == vacancy2)
    assert vacancy2 > vacancy1
