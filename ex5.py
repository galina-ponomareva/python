income = float(input("Please, enter your income: "))
expenses = float(input("Please, enter your expenses: "))

profit = income - expenses

if profit > 0:
    efficiency = profit / income
    print(f"Congratulations! Your business is profitable.\nProfit: {profit:.2f}\nEfficiency: {efficiency:.2f}")
    empl_number = int(input("Please, enter your number of employees: "))
    print(f"Profit per employee: {profit / empl_number:.2f}")
elif profit == 0:
    print("You break even.")
else:
    print(f"Your business is loss-making. Loss: {profit * (-1):.2f}")
