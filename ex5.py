# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.


def list_sum(list_num):
    for n, elem in enumerate(list_num):
        list_num[n] = float(elem)
    total = sum(list_num)
    return total


print('Для добавления к общей сумме вводите числа через пробел. Для выхода из программы нажмите "q".')
list_total = 0
total_sum = 0
q = 0

while True:
    user_list = input('').split()

    for i in user_list:
        if i.lower() == 'q':
            user_list.remove(i)
            list_total = list_sum(user_list)
            total_sum += list_total
            print(f'Сумма введенных чисел (Общая сумма)\n{list_sum(user_list)} ({total_sum})\n')
            q = 1
            break
        try:
            float(i)
        except ValueError:
            print('Вы хотите выйти из программы? Для выхода нажмите "q"')
            if input('') == 'q':
                user_list.remove(i)
                list_total = list_sum(user_list)
                total_sum += list_total
                print(f'Сумма введенных чисел (Общая сумма)\n{list_sum(user_list)} ({total_sum})\n')
                q = 1
                break
            else:
                user_list.remove(i)
                continue

    if q == 1:
        break
    list_total = list_sum(user_list)
    total_sum += list_total
    print(f'Сумма введенных чисел (Общая сумма)\n{list_sum(user_list)} ({total_sum})\n')
