import pytest
# from src import class_hh, utils, class_vacancies, class_filter_vacancies
from  Coursework_4.src import class_hh, utils, class_vacancies, class_filter_vacancies

@pytest.fixture()
def class_vaconcies_1():
    return class_vacancies.Vacancies("97098403",
        "Project Manager/Product manager",
        {
            "id": "1",
            "name": "Москва",
            "url": "https://api.hh.ru/areas/1"
        },{
            "from": 398243,
            "to": 398243,
            "currency": "RUR",
            "gross": False
        },{
            "id": "3749818",
            "name": "Bazilik Group",
            "url": "https://api.hh.ru/employers/3749818",
            "alternate_url": "https://hh.ru/employer/3749818",
            "logo_urls": None,
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3749818",
            "accredited_it_employer": False,
            "trusted": None
        },{
            "requirement": "Понимание кода (JS, <highlighttext>Python</highlighttext>) - на базовом уровне. Понимание как устроен бэк и фронт. UI/UX. Умение составлять SQL запросы, пользоваться...",
            "responsibility": "Анализировать бизнес требования, проводить системный анализ. Описывать тикет, вести его с разработчиком. Отвечать за сроки выхода задач. Отвечать за полноту..."
        },{
            "id": "remote",
            "name": "Удаленная работа"
        },{
                "id": "107",
                "name": "Руководитель проектов"
            },{
            "id": "between3And6",
            "name": "От 3 до 6 лет"
        },{
            "id": "full",
            "name": "Полная занятость"
        },
            "https://hh.ru/vacancy/97098403")

@pytest.fixture()
def class_vaconcies_2():
    return class_vacancies.Vacancies("96034351",
        "Junior Python разработчик",
        {
            "id": "2",
            "name": "Санкт-Петербург",
            "url": "https://api.hh.ru/areas/2"
        },{

            "from": 50000,
            "to": 50000,
            "currency": "RUR",
            "gross": False
        },{
            "id": "3749818",
            "name": "Bazilik Group",
            "url": "https://api.hh.ru/employers/3749818",
            "alternate_url": "https://hh.ru/employer/3749818",
            "logo_urls": None,
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3749818",
            "accredited_it_employer": False,
            "trusted": None
        },{
            "requirement": "Понимание кода (JS, <highlighttext>Python</highlighttext>) - на базовом уровне. Понимание как устроен бэк и фронт. UI/UX. Умение составлять SQL запросы, пользоваться...",
            "responsibility": "Анализировать бизнес требования, проводить системный анализ. Описывать тикет, вести его с разработчиком. Отвечать за сроки выхода задач. Отвечать за полноту..."
        },{
            "id": "fullDay",
            "name": "Полный день"
        },{
                "id": "96",
                "name": "Программист, разработчик"
            },{
            "id": "noExperience",
            "name": "Нет опыта"
        },{
            "id": "full",
            "name": "Полная занятость"
        },
            "https://hh.ru/vacancy/97098403")


@pytest.fixture()
def class_filter_vaconcies():
    return class_filter_vacancies.FilterVacancies([class_vaconcies_1,class_vaconcies_2])

def test_class_vacancies_1(class_vaconcies_1):
    assert class_vaconcies_1.id == "97098403"
    assert class_vaconcies_1.name == "Project Manager/Product manager"
    assert class_vaconcies_1.area["name"] == "Москва"

def test_class_vacancies_2(class_vaconcies_2):
    assert class_vaconcies_2.id == "96034351"
    assert class_vaconcies_2.name == "Junior Python разработчик"
    assert class_vaconcies_2.area["name"] == "Санкт-Петербург"



