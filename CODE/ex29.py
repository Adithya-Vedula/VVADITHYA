print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex29.py" + " ============")

#made by adithya
import string
print("Welcome to the Letter Guessing Game!")

while True:
    play_choice = input("Do you want to play the game? (Y/N): ")
    play_choice = play_choice.strip().upper()

    if play_choice == 'N':
        print("Thank you for playing! Goodbye.")
        break
    elif play_choice != 'Y':
        print("Please enter 'Y' to play or 'N' to exit.")
        continue

    print("Great! Try to guess the letters (A-Z). Enter 'Q' to quit the game.")
    guessed_letters = []

    while True:
        guess = input("Enter a letter: ").strip().upper()

        if guess == 'Q':
            print("Quitting the game. Goodbye!")
            

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
            else:
                guessed_letters.append(guess)
                print(f"You guessed: {guess}")
        else:
            print("Please enter a single letter (A-Z) or 'Q' to quit the game.")



