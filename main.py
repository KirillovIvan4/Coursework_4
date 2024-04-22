from src import class_hh, utils, class_vacancies, class_filter_vacancies
import json

keyword = input("Введите вакансию")
user_answer = False
while user_answer != True:
    page = input("""Введите сколько страниц загрузить.Максимум 20 страниц
    (на каждой странице 100 вакансий """)
    if page.isdigit() == True:
        page = int(page)
        if page <= 20:
            user_answer = True
        else:
            print("Такой страницы не существует")
    else:
        print("Введите число")

area_user = "Москва"


# Запись вакансий в файл vacancies.json
hh = class_hh.HH()
hh.upload_and_record_vacancies(keyword, page)

# Запись актуального курса валют в файл exchange_rates.json
utils.upload_exchange_rates()
# Список курса валют
exchange_rates = utils.get_dict_exchange_rates()

data_vacancies = utils.get_list()
list_vacancies = []

for i in range(len(data_vacancies)):
    vacancies = class_vacancies.Vacancies(
        data_vacancies[i]["id"],
        data_vacancies[i]["name"],
        data_vacancies[i]["area"],
        data_vacancies[i]["salary"],
        data_vacancies[i]["employer"],
        data_vacancies[i]["snippet"],
        data_vacancies[i]["schedule"],
        data_vacancies[i]["professional_roles"],
        data_vacancies[i]["experience"],
        data_vacancies[i]["employment"],
        data_vacancies[i]["alternate_url"],
)
    list_vacancies.append(vacancies)
# Редактирование вакансий. В зарплате, если salary = None, то добавляется {"to":0} , если to = 0 то to = from
for vacancies in list_vacancies:
    vacancies.editing_salary()
    vacancies.convert_currency_salary(exchange_rates)

# Объявление класса для фильтрования вакансий
filter_list_vacancies = class_filter_vacancies.FilterVacancies(list_vacancies)
# Объявление переменных необходимых в цикле
number_filter = ''
while number_filter != 9:
    print("""Выберите способ фильтрации вакансий
        1 - фильтровать по городу
        2 - фильтровать по зарплате
        3 - фильтровать по графику работы Полный день или Удаленная работа
        4 - фильтровать по необходимому опыту
        5 - фильтровать по занятости Стажировка, Частичная занятость или Полная занятость
        6 - показать список вакансий
        7 - Сохранить список вакансий в файле
        8 - Редактировать файл с вакансиями
        9 - завершить работу""")

    number_filter = input("Введите фильтр\n")
    if number_filter in ['1','2','3','4','5','6','7','8','9']:

        if number_filter == '1':
            area_user = input("Введите город\n")
            # Сортировка по городу
            filter_list_vacancies = class_filter_vacancies.FilterVacancies.filter_by_area( filter_list_vacancies.list_vacancies, area_user)
            print(filter_list_vacancies)

        if number_filter == '2':
            # Сортировка по зарплате
            filter_list_vacancies = class_filter_vacancies.FilterVacancies.filter_by_salary(list_vacancies)
            print("Зарплаты отсортированы по зарплате от большой к меньшей")

        if number_filter == '3':
            filter_schedule = input("""
            1 - Полный день
            2 - Удаленная работа\n""")
            if filter_schedule in ['1', '2']:
                if filter_schedule == '1':
                    schedule ="Полный день"
                if filter_schedule == '2':
                    schedule ="Удаленная работа"
                # Сортировка по графику работы Полный день или Удаленная работа
                filter_list_vacancies = class_filter_vacancies.FilterVacancies.filter_by_schedule(filter_list_vacancies.list_vacancies, schedule)
                print(filter_schedule)
                print(filter_list_vacancies)
            else:
                print("Выбран несуществующий фильтр")

        if number_filter == '4':
            filter_experience = int(input("""
            1 - Нет опыта
            2 - От 1 года до 3 лет
            3 - От 3 до 6 лет
            4 - Более 6 лет\n"""))
            if filter_experience in ['1', '2', '3', '4']:
                if filter_experience == '1':
                    experience = "Нет опыта"
                if filter_experience == '2':
                    experience = "От 1 года до 3 лет"
                if filter_experience == '3':
                    experience = "От 3 до 6 лет"
                if filter_experience == '4':
                    experience = "Более 6 лет"
                # Сортировка по необходимому опыту
                filter_list_vacancies = class_filter_vacancies.FilterVacancies.filter_by_experience(filter_list_vacancies.list_vacancies, experience)
                print(filter_list_vacancies)
            else:
                print("Выбран несуществующий фильтр")

        if number_filter == '5':
            filter_employment = int(input("""
            1 - Стажировка
            2 - Частичная занятость
            3 - Полная занятость\n"""))
            if filter_employment in ['1', '2', '3']:
                if filter_employment == '1':
                    employment = "Стажировка"
                if filter_employment == '2':
                    employment = "Частичная занятость"
                if filter_employment == '3':
                    employment = "Полная занятость"
                # Сортировка по необходимому опыту
                filter_list_vacancies = class_filter_vacancies.FilterVacancies.filter_by_employment(filter_list_vacancies.list_vacancies, employment)
                print(filter_list_vacancies)
            else:
                print("Выбран несуществующий фильтр")

        if number_filter == 6:
            answer_user = int(input("""
            1 - Показать весь список вакансий 
            2 - Показать топ n вакансий 
            """))
            if answer_user in ['1', '2']:
                if answer_user == 1:
                    print("sda")
                    for vacancies in filter_list_vacancies.list_vacancies:
                        print(vacancies)

                if answer_user == 2:
                    top_vacancies = int(input("Сколько вакансий показать?\n"))
                    filter_list_vacancies = class_filter_vacancies.FilterVacancies.top_vacancies (filter_list_vacancies.list_vacancies, top_vacancies)
                    for vacancies in filter_list_vacancies.list_vacancies:
                        print(vacancies)
            else:
                print("Выбран несуществующий фильтр")

        if number_filter == 7:
            print(utils.save_vacancies(filter_list_vacancies.list_vacancies))

        if number_filter == 8:
            answer_user = int(input("""
                    1 - Очистить список вакансий
                    2 - удалить одну вакансию по id
                    """))
            if answer_user in ['1', '2']:
                if answer_user == 1:
                    answer_user = "clear"
                    filter_list_vacancies = class_filter_vacancies.FilterVacancies.delite_vacancies(filter_list_vacancies.list_vacancies, answer_user)
                    utils.save_vacancies(filter_list_vacancies.list_vacancies)
                if answer_user == 2:
                    answer_user = input("""
                        Введите id вакансии
                        """)
                    filter_list_vacancies = class_filter_vacancies.FilterVacancies.delite_vacancies(filter_list_vacancies.list_vacancies, answer_user)
                    utils.save_vacancies(filter_list_vacancies.list_vacancies)
            else:
                print("Выбран несуществующий фильтр")

        if number_filter == 9:
            print("Завершить программу?")
            answer_user = input("y/n\n")
            if answer_user == "y":
               exit()
            else:
                number_filter = ""

    else:
        print("Выбран несуществующий фильтр")
