from datetime import date

# Два варианта добавления модулей:
from application.salary import calculate_salary
import application.db.people as db

# Два варианта вывода сегодняшней даты
if __name__ == '__main__':
    calculate_salary()
    db.get_employees(date.today())
    print(f"Сегодняшняя дата: {date.today()}")
