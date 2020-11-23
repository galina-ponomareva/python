from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_waste(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 36:
            self.__v = 36
        elif v > 72:
            self.__v = 72
        elif v % 2 != 0:
            self.__v = v + 1
        else:
            self.__v = v

    def fabric_waste(self):
        return f"Расход ткани для пальто размера {self.v} составит {(self.v / 23 + 0.5):.2f} п.м. " \
               f"при ширине отреза 150 см."


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 1.2:
            self.__h = 1.2
        elif h > 2.2:
            self.__h = 2.2
        else:
            self.__h = h

    def fabric_waste(self):
        return f"Расход ткани для костюма (рост {self.h} м) составит {(2 * self.h +0.3):.2f} п.м. " \
               f"при ширине отреза 150 см."


while True:
    try:
        size = int(input("Введите размер одежды: "))
        height = float(input("Введите рост: "))
        coat_1 = Coat(size)
        print(coat_1.fabric_waste())

        suit_1 = Suit(height)
        print(suit_1.fabric_waste())
        break
    except ValueError:
        print("Введите число.")
        continue
