from abc import ABC, abstractmethod
import json
from typing import Any
from src.job import Vacancy

class FileWorker(ABC):
    """
    Абстрактный класс для работы с файлами.
    """
    @abstractmethod
    def write(self, filename: str, data: Any):
        pass

    @abstractmethod
    def read(self, filename: str) -> Any:
        pass

class JSONSaver(FileWorker):
    """
    Класс для работы с JSON файлами.
    """
    def write(self, filename: str, data: Any):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def read(self, filename: str) -> Any:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def add_vacancy(self, vacancy: Vacancy, filename: str):
        data = self.read(filename)
        data.append(vacancy.__dict__)
        self.write(filename, data)

    def delete_vacancy(self, vacancy: Vacancy, filename: str):
        data = self.read(filename)
        data = [v for v in data if v['title'] != vacancy.title]
        self.write(filename, data)

if __name__ == '__main__':
    filename = 'test_vacancies.json'
    test_vacancy = Vacancy("Python Developer", "http://example.com", 100000, 150000, "Опыт работы от 3 лет")
    json_saver = JSONSaver()

    # Сохраняем вакансию в файл
    json_saver.write(filename, [test_vacancy.__dict__])
    print("Сохранено в файл.")

    # Читаем из файла
    vacancies = json_saver.read(filename)
    print("Прочитано из файла:", vacancies)

    # Добавляем вакансию
    json_saver.add_vacancy(test_vacancy, filename)
    print("Добавлено в файл.")

    # Удаляем вакансию
    json_saver.delete_vacancy(test_vacancy, filename)
    print("Удалено из файла.")
