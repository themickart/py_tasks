from 5.2 import print_vacancies
from 2.1.3 import main_pdf
import cProfile

data = input("Введите 'Вакансии' для формирование табличнх вакансии или 'Статистика' для формирования отчета: ")
if data == "Вакансии":
    cProfile.run("print_vacancies()")
    # print_vacancies()
elif data == "Статистика":
    cProfile.run("main_pdf()")
    # main_pdf()
