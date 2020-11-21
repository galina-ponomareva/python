# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

try:
    f_user_data = open("user_data.txt", 'r', encoding="utf-8")
    data = f_user_data.readlines()
    strings = len(data)
    words = [len(el.split()) for el in data]

    print(f"Количество строк: {strings}")
    for i, el in enumerate(words):
        print(f"В строке {i+1} - {el} слов")
    f_user_data.close()
except IOError as err:
    print(err)
