# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:

    days_months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def numerize(cls, str_date):
        num_list = str_date.split("-")
        try:
            day = int(num_list[0])
            month = int(num_list[1])
            year = int(num_list[2])
            return cls(day, month, year)
        except ValueError:
            print("Format error. Dd, mm and yyyy should be integer numbers.")

    @staticmethod
    def validate(my_date):
        if not 1 <= my_date.month <= 12:
            return "Invalid data. Check mm value."
        elif not 1 <= my_date.day <= Date.days_months.get(my_date.month):
            return "Invalid data. Check dd value."
        elif not 1 <= my_date.year <= 9999:
            return "Invalid data. Check yyyy value."
        else:
            return f"Date validated. You've entered: {my_date.day}-{my_date.month}-{my_date.year}."


user_date = Date.numerize(input("Enter the date using format dd-mm-yyyy:\n"))
print(Date.validate(user_date))
