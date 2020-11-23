# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname, sep=" ")

    def get_total_income(self):
        print(self._Worker__income.get("wage") + self._Worker__income.get("bonus"))


workers = []

while True:
    if input("Добавить сотрудника? да/нет\n") == "нет":
        break
    try:
        w_name = input("Введите имя: ")
        w_surname = input("Введите фамилию: ")
        w_position = input("Введите должность: ")
        w_wage = float(input("Введите оклад: "))
        w_bonus = float(input("Введите премию: "))

        worker = Position(w_name, w_surname, w_position, w_wage, w_bonus)
        workers.append(worker)
        continue
    except ValueError:
        print("Для параметров 'оклад' и 'премия' введите число.")
        continue

for w in workers:
    print(w.surname, w.position, w._Worker__income.get("wage"))
    w.get_full_name()
    w.get_total_income()
