# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def sum_max_two(arg_1, arg_2, arg_3):
    """Возвращает сумму двух наибольших из трех аргументов."""
    arg_list = [arg_1, arg_2, arg_3]
    arg_list.remove(min(arg_list))
    result = sum(arg_list)
    return result


while True:
    try:
        num_1 = int(input('Введите первое число: '))
        num_2 = int(input('Введите второе число: '))
        num_3 = int(input('Введите третье число: '))

        print(f"Сумма наибольших двух чисел: {sum_max_two(num_1, num_2, num_3)}")
        break
    except ValueError:
        print("Введите число.")
        continue
