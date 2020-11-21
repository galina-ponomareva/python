# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f_user_data = open("user_data.txt", 'w', encoding="utf-8")

print("Вводите данные построчно для записи в файл. Для завершения ввода оставьте строку пустой и нажмите Enter.")

while True:
    user_content = input("")
    if not user_content:
        break
    f_user_data.write(f"{user_content}\n")

f_user_data.close()
