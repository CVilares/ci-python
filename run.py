# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def guessing_game():
    """
    Main function of the guessing game.
    """
    number = random.randint(1, 100)
    """
    The 'random.randint(a, b)' function is used to generate a random integer between 'a' and 'b'.
    In this case, it generates a random number between 1 and 100 and assigns it to the 'number' variable.
    """
    attempts = 0
    """
    This line attempts = 0 initializes the attempts variable and sets its initial value to 0.
    """

    while True:
        # Get the user's guess
        guess = input("Enter your guess: ")

        

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

guessing_game()
