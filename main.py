from src.api import HeadHunterAPI
from src.job import Vacancy
from src.file_worker import JSONSaver
from src.job_manager import JobManager

def filter_vacancies(vacancies, keywords):
    """
    Фильтрация вакансий по ключевым словам.
    """
    return [vacancy for vacancy in vacancies if any(keyword.lower() in (vacancy.description or '').lower() for keyword in keywords)]

def get_vacancies_by_salary(vacancies, salary_range):
    """
    Фильтрация вакансий по диапазону зарплат.
    """
    min_salary, max_salary = map(int, salary_range.split('-'))
    return [vacancy for vacancy in vacancies if isinstance(vacancy.salary_from, int) and min_salary <= vacancy.salary_from <= max_salary]

def sort_vacancies(vacancies):
    """
    Сортировка вакансий по зарплате.
    """
    return sorted(vacancies, key=lambda vacancy: vacancy.salary_from, reverse=True)

def get_top_vacancies(vacancies, top_n):
    """
    Получение топ N вакансий.
    """
    return vacancies[:top_n]

def print_vacancies(vacancies):
    """
    Вывод вакансий на экран.
    """
    for vacancy in vacancies:
        print(vacancy)

def user_interaction():
    """
    Функция для взаимодействия с пользователем через консоль.
    """
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

if __name__ == "__main__":
    user_interaction()
