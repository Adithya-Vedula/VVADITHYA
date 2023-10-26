print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex28.py" + " ============")

# made by aditya
import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Beatrice, you need to guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Try a higher number.")
    elif guess > secret_number:
        print("Try a lower number.")
    else:
        print(f"Congratulations, Beatrice! You guessed the correct number, which is {secret_number}. It took you {attempts} attempts.")
        break
