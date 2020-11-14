# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary_count():
    try:
        name, rate, hours, bonus = argv
    except ValueError:
        return 'Введите три параметра в следующем порядке: ставка в час, выработка в час, премия.'
    try:
        rate = int(rate)
        hours = int(hours)
        bonus = int(bonus)
    except ValueError:
        return 'Введите целочисленные параметры: ставка в час, выработка в час, премия.'
    salary = (rate * hours) + bonus
    return salary


print(f"Заработная плата сотрудника:\n{salary_count()}")
