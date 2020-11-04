num = 0
max = 0

while num <= 0:
    num = int(input("Enter positive integer number: "))

while num > 0:
    if num % 10 > max:
        max = num % 10
    num //= 10

print(f"Maximum digit: {max}")
