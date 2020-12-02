# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.re == 0:
            return f"{self.im}i"
        elif self.im == 0:
            return f"{self.re}"
        elif self.im < 0:
            return f"{self.re} - {abs(self.im)}i"
        else:
            return f"{self.re} + {self.im}i"

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)


print("*** Complex numbers calculator ***")
while True:
    try:
        re_1 = float(input("Complex number 1. Enter real part: "))
        im_1 = float(input("Complex number 1. Enter imaginary part: "))
        re_2 = float(input("Complex number 2. Enter real part: "))
        im_2 = float(input("Complex number 2. Enter imaginary part: "))
    except ValueError:
        print("Enter a number.")
        continue
    else:
        complex_1 = Complex(re_1, im_1)
        complex_2 = Complex(re_2, im_2)
        print(f"You have entered the following complex numbers:\n{complex_1}\n{complex_2}")
        while True:
            operation = input("Press '1' to add the numbers. Press '2' to multiply the numbers. Press '3' to exit.\n")
            if operation == '1':
                print(complex_1 + complex_2)
                continue
            elif operation == '2':
                print(complex_1 * complex_2)
                continue
            elif operation == '3':
                break
            else:
                continue
        break
