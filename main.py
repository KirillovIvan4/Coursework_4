from src import class_hh
# Запись вакансий в файл vacancies.json
keyword = input("Введите вакинсию которую вы ищите \n")
number_page = input("Введите номер страници с сайта  \n")
hh = class_hh.HH()
hh.upload_and_record_vacancies(keyword, number_page)

print("""Выберите способ фильтрации вакансий
1 - фильтровать по городу
2 - фильтровать по зарплате
3 - фильтровать по занятости
4 - фильтровать по расписанию""")
