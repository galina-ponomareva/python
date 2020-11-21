# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open("numbers.txt", 'w+', encoding="utf-8") as f_num:
    nums = [str(randint(-100, 100)) for el in range(0, 20)]
    f_num.write(' '.join(nums))
    f_num.seek(0)

    data = [int(el) for el in f_num.readline().split()]
    print(f"Сумма чисел в файле: {sum(data)}")
