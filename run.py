import random
"""
"""

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
    """
    """

def play_game():
    """
    Play the guessing game.
    """
     
    number = random.randint(1, 100)
    """
    Generate a random number between 1 and 100
    """
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while True:
        
        guess = input("Enter your guess: ")
        """
        Get the user's guess
        """

        if not guess.isdigit():
            """
             Check if the input is a valid number
            """ 
            print("Invalid input. Please enter a valid number.")
            continue

        guess = int(guess)
        """
        tranform guess into a integer
        """

        attempts += 1
        """
        increase the attempts
        """

        if guess < 1 or guess > 100:
            """
             Check if the guess is within the valid range
            """
             
            print("Number must be between 1-100, please guess again.")
        elif guess < number:
            """
            block is executed when the user's guess is less than the randomly generated number
            """
            print("Too low. Try again!")
        elif guess > number:
            """
            block is executed when the user's guess is greater than the randomly generated number
            """
            print("Too high. Try again!")
        else:
            """
            block is executed when the user's guess is equal to the randomly generated number
            """
            
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
        """
        Get the user's choice
        """
        choice = input("Enter your choice:").upper()

        if choice == "R":
            """
            Display the rules
            """
            display_rules()
        elif choice == "P":
            """
             Play the game
            """
            play_game()
        elif choice == "Q":
            """
            Quit the game
            """
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please try again.")

start_game()
