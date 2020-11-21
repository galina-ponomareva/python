# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import translators as ts

try:
    with open("text_4.txt", 'r', encoding="utf-8") as f_eng:
        eng_num = f_eng.readlines()
        rus_num = [ts.translate_html(el.split()[0], translator=ts.google, to_language='ru') + ' '
                   + ' '.join(el.split()[1:3]) + '\n' for el in eng_num]

    with open("text_4_ru.txt", 'w', encoding="utf-8") as f_rus:
        f_rus.writelines(rus_num)
except IOError as err:
    print(err)
