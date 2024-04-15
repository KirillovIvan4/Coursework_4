from src import class_hh, class_parser.

keyword = input("Введите вакинсию которую вы ищите")
number_page = int(input("Введите номер страници с сайта"))
hh = class_hh.HH()
hh.upload_and_record_vacancies(keyword, number_page)