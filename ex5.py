# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

rating = [11, 8, 8, 5, 4]

while True:
    if input("Enter new rating value? y/n\n") == "y":
        new_item = int(input("Please enter new rating value: "))
        for i in rating:
            if i < new_item:
                rating.insert(rating.index(i), new_item)
                break
            elif new_item > 0:
                rating.append(new_item)
                break
        print(rating)
    else:
        print(rating)
        break
