from math import ceil


class Cell:

    def __init__(self, cells_num):
        self.cells_num = cells_num

    @property
    def cells_num(self):
        return self.__cells_num

    @cells_num.setter
    def cells_num(self, cells_num):
        if cells_num < 0:
            self.__cells_num = 0
        else:
            self.__cells_num = cells_num

    def __str__(self):
        return f"{self.__cells_num}"

    def __add__(self, other):
        result = self.__cells_num + other.__cells_num
        result = Cell(result)
        return result

    def __sub__(self, other):
        if self.__cells_num < other.__cells_num:
            return "Разность не определена."
        else:
            result = self.__cells_num - other.__cells_num
            result = Cell(result)
            return result

    def __mul__(self, other):
        result = self.__cells_num * other.__cells_num
        result = Cell(result)
        return result

    def __truediv__(self, other):
        if other.__cells_num == 0:
            return "Деление на нулевую клетку не определено."
        else:
            result = ceil(self.__cells_num / other.__cells_num)
            result = Cell(result)
            return result

    def make_order(self, row):
        string = chr(152) * row
        total = [string for _ in range(0, self.__cells_num // row)]
        if self.__cells_num % row != 0:
            total.append(chr(152) * (self.__cells_num % row))
        return "\n".join(total)


cell_1 = Cell(5)
cell_2 = Cell(2)

print(cell_1, cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

cell_3 = Cell(-3)

print(cell_3)
print(cell_1 / cell_3)

print(cell_1.make_order(2))
print(cell_1.make_order(6))

cell_4 = Cell(101)
print(cell_4.make_order(12))
