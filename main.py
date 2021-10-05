from datetime import date

# Два варианта добавления модулей:
from application.salary import calculate_salary
import application.db.people as db


if __name__ == '__main__':
    calculate_salary()
    db.get_employees()
    print(f"Сегодняшняя дата: {date.today()}")
