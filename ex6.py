a = float(input("Please, enter the first day distance: "))
b = float(input("Please, enter the goal distance: "))

while a <= 0 or b <= 0:
    print("Please, enter a positive number.")
    a = float(input("Please, enter the first day distance: "))
    b = float(input("Please, enter the goal distance: "))

day = 1

while a < b:
    a *= 1.1
    day += 1

print(f"Goal distance will be reached on day {day}")
