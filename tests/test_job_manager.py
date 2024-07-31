import pytest
import os
from src.job_manager import JobManager
from src.job import Vacancy
from src.file_worker import JSONSaver

@pytest.fixture
def job_manager():
    return JobManager(JSONSaver())

@pytest.fixture
def test_file():
    return "tests/test_vacancies.json"

def teardown_method(method):
    if os.path.exists("tests/test_vacancies.json"):
        os.remove("tests/test_vacancies.json")

def test_add_and_filter_job(job_manager):
    job = Vacancy("Job 1", "http://example.com", 1000, 2000, "Python Developer")
    job_manager.add_job(job)
    assert len(job_manager.jobs) == 1
    filtered_jobs = job_manager.filter_jobs_by_keyword("Python")
    assert len(filtered_jobs) == 1
    assert filtered_jobs[0].title == "Job 1"

def test_save_and_load_jobs(job_manager, test_file):
    job = Vacancy("Job 1", "http://example.com", 1000, 2000, "Python Developer")
    job_manager.add_job(job)
    job_manager.save_jobs_to_file(test_file)
    job_manager.load_jobs_from_file(test_file)
    assert len(job_manager.jobs) == 1
    assert job_manager.jobs[0].title == "Job 1"

if __name__ == '__main__':
    pytest.main()
