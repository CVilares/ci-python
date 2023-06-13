# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def display_rules():
    """
    Display the rules of the game.
    """
    print("===================================")
    print("Guessing Game - Rules")
    print("===================================")
    print("1. The computer will randomly choose a number between 1 and 100.")
    print("2. You have to guess the chosen number.")
    print("3. After each guess, the computer will provide feedback: 'Too low' or 'Too high'.")
    print("4. Keep guessing until you guess the correct number.")
    print("===================================\n")

def play_game():
    """
    Play the guessing game.
    """
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while True:
        # Get the user's guess
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            # Check if the input is a valid number
            print("Invalid input. Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < 1 or guess > 100:
            # Check if the guess is within the valid range
            print("Number must be between 1-100, please guess again.")
        elif guess < number:
            print("Too low. Try again!")
        elif guess > number:
            print("Too high. Try again!")
        else:
            # Correct guess
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    print("The game is over.")

def start_game():
    """
    Start the guessing game.
    """
    print("Welcome to the Guessing Game!")
    print("Press 'R' to read the rules.")
    print("Press 'P' to play the game.")
    print("Press 'Q' to quit the game.")

    while True:
        # Get the user's choice
        choice = input("Enter your choice:").upper()

        if choice == "R":
            # Display the rules
            display_rules()
        elif choice == "P":
            # Play the game
            play_game()
        elif choice == "Q":
            # Quit the game
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please try again.")

start_game()
