from src import class_hh, utils, class_vacancies, class_filter_vacancies
# Запись вакансий в файл vacancies.json
keyword = input("Введите вакинсию которую вы ищите\n")
number_page = input("Введите номер страници с сайта\n")
hh = class_hh.HH()
hh.upload_and_record_vacancies(keyword, number_page)

data_vacancies = utils.get_list()
list_vacancies = []
for i in range(len(data_vacancies)):
    vacancies = class_vacancies.Vacancies(data_vacancies[i]["id"], data_vacancies[i]["name"], data_vacancies[i]["area"])
    list_vacancies.append(vacancies)


filter_list_vacancies = class_filter_vacancies.FilterVacancies(list_vacancies)

print(filter_list_vacancies)
filter_list_vacancies = class_filter_vacancies.FilterVacancies.filter_by_area(filter_list_vacancies.list_vacancies, "Алматы")
print(filter_list_vacancies)
# print(len(list_vacancies), list_vacancies)

# 1 - area - город по умолчанию Москва
# 2 - from - зарплата "от" по умолчанию 0 to - зарплата "к" по умолчанию равна from
# 3 - fullDay - занятость на полный день part - занятость на
dict_filter = {1:"area", 2:{1:"from", 2:"to"}, 3:{1:"fullDay", 2:"part" }, 4:{1:"full", 2:"flexible"},5:"exit"}

print()
# list_filter = {}
# number_filter = ''
# while number_filter != 5:
#     print("""Выберите способ фильтрации вакансий
#         1 - фильтровать по городу
#         2 - фильтровать по зарплате
#         3 - фильтровать по занятости
#         4 - фильтровать по расписанию
#         5 - показать список вакансий""")
#
#     number_filter = int(input("Введите фильтр\n"))
#
#     if number_filter not in list_filter:
#         area = ''
#         salary = ''
#         if number_filter == 1:
#             area = input("Введите город")
#         if number_filter == 2:
#
#
#         list_filter[dict_filter[number_filter]] = input()
#
#     else:
#         print("Этот фильтр уже применен")
# print(list_filter)
# quantity =  int(input("Введите фильтр\n"))
area = "Ярославль"