from main import *
from package import *

if __name__ == '__main__':
    calculate_salary()
    db.get_employees()
    print(f"Сегодняшняя дата: {date.today()}")

"""
Я не совсем понял задание #4, что такое packege, это папка из которой
нужно вызвать все функции?
Я вызвал модуль main и тогда смог вызвать все функции, по другому у меня ничего не получилось
"""