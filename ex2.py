# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroError(Exception):

    def __init__(self, text):
        self.text = text


while True:
    user_data = input("Enter a dividend and a divider, use space as a separator.\n").split()
    try:
        if float(user_data[1]) == 0:
            raise ZeroError("Zero division is not defined.")
        result = round(float(user_data[0]) / float(user_data[1]), 4)
    except (IndexError, ValueError, ZeroError) as err:
        print(err)
        continue
    else:
        print(f"Result: {result}")
        break
