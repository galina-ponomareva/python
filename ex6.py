# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
# и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.

menu = "*** База данных товаров ***\n* добавить товар - введите 'i'\n* просмотреть данные о товарах - введите 'd'\n" \
       "* просмотреть аналитику - введите 'a'\n* завершить работу - введите 'q'\n"
goods = []

while True:
    request = input(menu)
    if request == "i":
        item = input("Введите название товара: ")
        price = float(input("Введите цену: "))
        quantity = int(input("Введите количество: "))
        unit = input("Введите единицу измерения: ")
        item_dict = {"название": item, "цена": price, "количество": quantity, "единица измерения": unit}
        goods.append((len(goods) + 1, item_dict))
        continue
    elif request == "d":
        if not goods:
            print("Пока не введено ни одного товара")
            continue
        else:
            print(goods)
            continue
    elif request == "a":
        if not goods:
            print("Пока не введено ни одного товара")
            continue
        else:
            item_values = []
            price_values = []
            quantity_values = []
            unit_values = []

            for i in goods:
                item_values.append(i[1].get("название"))
                price_values.append(i[1].get("цена"))
                quantity_values.append(i[1].get("количество"))
                unit_values.append(i[1].get("единица измерения"))

            # Убираем дубли из списков значений характеристик товаров.
            for i in item_values:
                j = 1
                while j < item_values.count(i):
                    item_values.remove(i)
                    j += 1

            for i in price_values:
                j = 1
                while j < price_values.count(i):
                    price_values.remove(i)
                    j += 1

            for i in quantity_values:
                j = 1
                while j < quantity_values.count(i):
                    quantity_values.remove(i)
                    j += 1

            for i in unit_values:
                j = 1
                while j < unit_values.count(i):
                    unit_values.remove(i)
                    j += 1
            #

            analytics = {"название": item_values, "цена": price_values, "количество": quantity_values,
                         "единица измерения": unit_values}
            print(analytics)
            continue
    elif request == "q":
        break
    else:
        continue
