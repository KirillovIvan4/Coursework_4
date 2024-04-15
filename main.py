from src import class_hh

keyword = input("Введите вакинсию которую вы ищите \n")
number_page = int(input("Введите номер страници с сайта  \n"))
hh = class_hh.HH()
hh.upload_and_record_vacancies(keyword, number_page)
