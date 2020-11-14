# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
# nice авп ъghj jапро hjjпаро вапрghgh cool

def int_func(string):
    words_list = string.split()
    new_words_list = words_list.copy()
    for i in words_list:
        letters_list = list(i)
        for j in letters_list:
            if 97 <= ord(j) <= 122:
                continue
            else:
                new_words_list.remove(i)
                break
    for w, elem in enumerate(new_words_list):
        new_words_list[w] = elem.title()
    new_string = " ".join(new_words_list)
    return new_string


user_string = input("Введите строку из слов, разделенных пробелом:\n").lower()
print(int_func(user_string))
