# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def div(dividend, divider):
    """Возвращает частное от деления, округленное до 3 знака после запятой."""
    try:
        quot = round(dividend / divider, 3)
        return quot
    except ZeroDivisionError:
        return "Деление на ноль не определено."


while True:
    try:
        num_1 = float(input("Введите делимое: "))
        num_2 = float(input("Введите делитель: "))
        print(div(num_1, num_2))
        break
    except ValueError:
        print("Введите число.")
        continue
