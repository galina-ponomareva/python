# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open("text_7.txt", 'r', encoding="utf-8") as read_f:
    data = read_f.readlines()
    profit_dict = {el.split()[0]: int(el.split()[2]) - int(el.split()[3]) for el in data}
    profitable = [el for el in profit_dict.values() if el >= 0]
    average_profit = {"average_profit": sum(profitable) / len(profitable)}

with open("text_777.json", 'w', encoding="utf-8") as write_f:
    json.dump([profit_dict, average_profit], write_f, ensure_ascii=False, indent=4, separators=(", ", ": "))
