# Job Vacancies Project

Этот проект предназначен для получения, обработки и управления вакансиями с платформы HeadHunter. 

## Структура проекта

project_folder
│
├── data
│ └── vacancies.json # JSON файл для хранения вакансий
│
├── src # Исходный код проекта
│ ├── api.py # Модуль для работы с API HeadHunter
│ ├── job.py # Модуль для работы с вакансиями
│ ├── file_worker.py # Модуль для работы с файлами
│ ├── job_manager.py # Модуль для управления вакансиями
│
├── tests # Тесты для проекта
│ ├── test_job.py # Тесты для модуля job.py
│ ├── test_job_manager.py # Тесты для модуля job_manager.py
│
├── main.py # Основной файл для запуска приложения
└── pyproject.toml # Конфигурационный файл Poetry


## Установка

### Шаг 1: Установите Poetry

Если Poetry еще не установлен на вашем компьютере, установите его с помощью следующей команды:



poetry install

poetry add --dev pytest

poetry run python main.py

poetry run pytest

Структура кода
src/api.py
Модуль для работы с API HeadHunter. Содержит класс HeadHunterAPI, который реализует методы для получения вакансий по ключевому слову.

src/job.py
Модуль для работы с вакансиями. Содержит класс Vacancy, который представляет вакансию и методы для преобразования данных из JSON в объекты вакансий.

src/file_worker.py
Модуль для работы с файлами. Содержит абстрактный класс FileWorker и его реализацию JSONSaver, которая позволяет сохранять и загружать вакансии из JSON файла.

src/job_manager.py
Модуль для управления вакансиями. Содержит класс JobManager, который предоставляет методы для добавления, удаления, фильтрации и сортировки вакансий.

tests/test_job.py
Тесты для модуля job.py, написанные с использованием pytest.

tests/test_job_manager.py
Тесты для модуля job_manager.py, написанные с использованием pytest.

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.fetch_jobs("Python")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Пример работы конструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "", 100000, 150000, "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy, "data/vacancies.json")
json_saver.delete_vacancy(vacancy, "data/vacancies.json")

Взаимодействие с пользователем
Пример функции для взаимодействия с пользователем через консоль:

def user_interaction():
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()
    job_manager = JobManager(json_saver)

    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.fetch_jobs(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    filename = "data/vacancies.json"
    json_saver.write(filename, [vac.__dict__ for vac in vacancies_list])

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print_vacancies(top_vacancies)
