import random


def clear_screen():
    """
    Clears the screen.
    """
    print('\033c')


def display_rules():
    """
    Display the rules of the game.
    """
    print("===================================")
    print("Guessing Game - Rules")
    print("===================================")
    print("1. The computer will randomly choose a number between 1 and 300.")
    print("1. The computer will let you choose between 3 levels.")
    print("2. You have to guess the chosen number.")
    print("3. The computer provides feedback: 'Too low' or 'Too high'.")
    print("4. Keep guessing until you guess the correct number.")
    print("===================================\n")


def play_game(A, B):
    """
    Play the guessing game.
    """
    number = random.randint(A, B)
    # Generate a random number between A and B
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("")
    print(f"Try to guess the number between {A} and {B}.")

    while True:
        # This loop will repeat until we get the correct guess
        print("")
        guess = input("Enter your guess: ")
        # Get the user's guess

        if not guess.isdigit():
            # Check if the input is a valid number
            print("Invalid input. Please enter a valid number.")
            continue

        guess = int(guess)
        # Transform guess into an integer

        attempts += 1
        # Increase the attempts

        if guess < A or guess > B:
            print(f"Number must be between {A}-{B}, please guess again.")
            # 
        elif guess < number:
            # Block is executed when the user's guess is less than the randomly generated number
            print("Too low. Try again!")
        elif guess > number:
            # Block is executed when the user's guess is greater than the randomly generated number
            print("Too high. Try again!")
        else:
            # Block is executed when the user's guess is equal to the randomly generated number
            print(f"Congratulations! You took {attempts} attempts.")
            break

    print("The game is over.")
    # When the loop is over, this message will be printed


def start_game():
    """
    Start the guessing game.
    """
    clear_screen()
    print("Welcome to the Guessing Game!")

    while True:
        # Get the user's choice
        print("")
        print("Press 'R' to read the rules.")
        print("Press 'P' to play the game.")
        print("Press 'Q' to quit the game.")
        print("")

        choice = input("Enter your choice:").upper().strip()
        # this methods will convert all characters
        # into uppercase and remove whitespaces

        print("")
        if choice == "R":
            display_rules()
        elif choice == "P":
            print("")
            print("Select the level:")
            print("")
            print("'E' to play Easy (1-50)")
            print("'M' to play Medium (1-100)")
            print("'P' to play Pro (1-300)")
            print("")
            level_choice = input("Enter the level: ").upper().strip()
            # this methods will convert all characters
            # into uppercase and remove whitespaces

            if level_choice == "E":
                play_game(1, 50)
            elif level_choice == "M":
                play_game(1, 100)
            elif level_choice == "P":
                play_game(1, 300)
            else:
                print("Invalid level choice. Please try again.")

        elif choice == "Q":
            print("Exiting the game.")
            break
        else:
            print("")
            print("Invalid choice. Please try again.")


start_game()
