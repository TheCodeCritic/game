# Guess the number
import random

num = random.randint(1,999)
numGuessed = False

while numGuessed == False:
    guess = int(input("Guess the number: "))
    if guess > num:
        print("Lower")
    elif guess < num:
        print("Higher")
    elif guess == num:
        numGuessed = True

print(f"Correct! The answer is {num}!")
