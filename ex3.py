n = input("Enter integer number n: ")

while int(n) < 0:
    print("Please, enter a positive integer.")
    n = input("Number n: ")

nn = n + n
nnn = n + n + n
total = int(n) + int(nn) + int(nnn)

print(f"n + nn + nnn = {total}")
