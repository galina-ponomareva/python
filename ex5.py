# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        print(f"Рисуем ручкой {self.title}.")


class Pencil(Stationery):

    def draw(self):
        print(f"Рисуем карандашом {self.title}.")


class Handle(Stationery):

    def draw(self):
        print(f"Рисуем маркером {self.title}.")


stationery = Stationery("0.3 мм")
stationery.draw()

pen = Pen("0.7 мм")
pen.draw()

pencil = Pencil("0.4 мм")
pencil.draw()

handle = Handle("3 мм")
handle.draw()
