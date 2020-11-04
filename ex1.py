print("Welcome to the riddle game!")

score = 0

print("Let's start guessing. Try this one:\nHow many months of the year have 28 days?")
user_answer = input("Your answer: ")
if user_answer.lower() == "all" or user_answer.lower() == "all of them":
    print("Correct! Next try?")
    score += 1
else:
    print("Nope. Try another one.")

print("It belongs to you, but your friends use it more. What is it?")
user_answer = input("Your answer: ")
if user_answer.lower() == "name" or user_answer.lower() == "your name":
    print("Correct! Next try?")
    score += 1
else:
    print("Nope. Try another one.")

print("Kate’s mother has three children: Snap, Crackle and ___?")
user_answer = input("Your answer: ")
if user_answer.lower() == "kate":
    print("Correct!")
    score += 1
else:
    print("Nope.")

print(f"Hope you've had a great time! Your score: {score} correct answers.")
