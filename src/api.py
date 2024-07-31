from abc import ABC, abstractmethod
import requests
from typing import List, Dict, Any

class JobAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        pass

class HeadHunterAPI(JobAPI):
    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": search_query,
            "area": "113",
            "per_page": "100"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()["items"]
