# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn",
                "autumn", "winter"]
seasons_dict = {"January": "winter", "Jan": "winter", "February": "winter", "Feb": "winter", "March": "spring",
                "Mar": "spring", "April": "spring", "Apr": "spring", "May": "spring", "June": "summer", "Jun": "summer",
                "July": "summer", "Jul": "summer", "August": "summer", "Aug": "summer", "September": "autumn",
                "Sep": "autumn", "October": "autumn", "Oct": "autumn", "November": "autumn", "Nov": "autumn",
                "December": "winter", "Dec": "winter"}

user_month = input("To learn the season enter month name or number: ")
print(
    f"{seasons_list[int(user_month) - 1] if user_month.isdigit() else seasons_dict.get(user_month.title())}")
