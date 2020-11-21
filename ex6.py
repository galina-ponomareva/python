# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

try:
    with open("text_6.txt", 'r', encoding="utf-8") as f_tt:
        timetable = [el for el in f_tt.readlines()]
        tt_keys = [list(el.split()[0]) for el in timetable]
        for el in tt_keys:
            el.remove(':')
        tt_keys = [''.join(el) for el in tt_keys]

        tt_values = [list(el) for el in timetable]
        for i, el in enumerate(tt_values):
            el = [a for a in el if 48 <= ord(a) <= 57 or ord(a) == 32]
            tt_values[i] = (''.join(el)).split()
            tt_values[i] = [int(j) for j in tt_values[i]]
        tt_values = [sum(el) for el in tt_values]

        tt_dict = {k: v for k, v in zip(tt_keys, tt_values)}

        print(tt_dict)

except IOError as err:
    print(err)
