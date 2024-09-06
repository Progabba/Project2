from abc import ABC, abstractmethod
import requests
from typing import List, Dict, Any

class JobAPI(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями.
    """
    @abstractmethod
    def fetch_jobs(self, keyword: str) -> List[Dict[str, Any]]:
        pass

class HeadHunterAPI(JobAPI):
    """
    Класс для работы с API HeadHunter.
    """
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'area': 113, 'page': 0, 'per_page': 100}  # area 113 = Russia
        self.vacancies = []

    def fetch_jobs(self, keyword: str) -> List[Dict[str, Any]]:
        self.params['text'] = keyword
        self.vacancies = []
        self.params['page'] = 0

        while self.params['page'] < 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            response.raise_for_status()
            vacancies = response.json().get('items', [])
            if not vacancies:
                break
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies

if __name__ == '__main__':
    hh_api = HeadHunterAPI()
    jobs = hh_api.fetch_jobs('Python Developer')
    print(f"Найдено {len(jobs)} вакансий.")
    for job in jobs[:5]:  # Печатаем первые 5 вакансий для примера
        print(job)
