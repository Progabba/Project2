from typing import List
from src.job import Vacancy
from src.file_worker import JSONSaver

class JobManager:
    """
    Класс для управления вакансиями.
    """
    def __init__(self, file_worker: JSONSaver):
        self.file_worker = file_worker
        self.jobs: List[Vacancy] = []

    def add_job(self, job: Vacancy):
        self.jobs.append(job)

    def save_jobs_to_file(self, filename: str):
        data = [job.__dict__ for job in self.jobs]
        self.file_worker.write(filename, data)

    def load_jobs_from_file(self, filename: str):
        data = self.file_worker.read(filename)
        self.jobs = [Vacancy(**item) for item in data]

    def filter_jobs_by_keyword(self, keyword: str) -> List[Vacancy]:
        return [job for job in self.jobs if keyword.lower() in job.description.lower()]

    def get_top_n_jobs_by_salary(self, n: int) -> List[Vacancy]:
        return sorted(self.jobs, key=lambda job: job.salary_from, reverse=True)[:n]

    def remove_job(self, job: Vacancy):
        self.jobs.remove(job)

if __name__ == '__main__':
    filename = 'test_jobs.json'
    test_vacancy = Vacancy("Python Developer", "http://example.com", 100000, 150000, "Опыт работы от 3 лет")
    json_saver = JSONSaver()
    job_manager = JobManager(json_saver)

    # Добавляем вакансию и сохраняем в файл
    job_manager.add_job(test_vacancy)
    job_manager.save_jobs_to_file(filename)
    print("Вакансия сохранена в файл.")

    # Загружаем вакансии из файла
    job_manager.load_jobs_from_file(filename)
    print("Вакансии загружены из файла:", job_manager.jobs)

    # Фильтрация вакансий по ключевому слову
    filtered_jobs = job_manager.filter_jobs_by_keyword("Python")
    print("Отфильтрованные вакансии:", filtered_jobs)

    # Получение топ вакансий по зарплате
    top_jobs = job_manager.get_top_n_jobs_by_salary(1)
    print("Топ вакансий по зарплате:", top_jobs)

    # Удаление вакансии
    job_manager.remove_job(test_vacancy)
    print("Вакансия удалена.")
