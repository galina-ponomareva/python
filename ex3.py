# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

try:
    with open("text_3.txt", 'r', encoding="utf-8") as f_sal:
        data = {el.split()[0]: float(el.split()[1]) for el in f_sal.readlines()}
        print("Сотрудники с окладом менее 20000:")
        for i in data.keys():
            if data.get(i) < 20000:
                print(i)
        print(f"Средний доход: {sum(data.values()) / len(data.values())}")

except IOError as err:
    print(err)
