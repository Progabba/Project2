from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.saver import JSONSaver
from src.utils import filter_vacancies, get_vacancies_by_salary, get_top_vacancies, print_vacancies

def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies_json = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies_json)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (например, 100000-150000): ")

    try:
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

        print_vacancies(top_vacancies)
    except ValueError:
        print("Ошибка: Диапазон зарплат должен быть в формате 'min-max'")

if __name__ == "__main__":
    user_interaction()
