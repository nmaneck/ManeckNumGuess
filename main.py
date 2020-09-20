import random

# Note random.randint is inclusive for both lower and upper endpoint
# See: https://docs.python.org/3/library/random.html
correctNum = random.randint(1, 100)

# Creates set of acceptable quit commands for later comparison
quitCommands = {"Q", "q", "Quit", "QUIT", "quit"}

# Initializes the current guess and the number of guesses so far at 0

guess = 0
numGuesses = 0

# Defines a function to return singular for 1 and plural for more than 1
# (This was probably not strictly necessary...)
def guessSoFar():
    if numGuesses == 1:
        return "1 guess"
    elif numGuesses > 1:
        return f"{numGuesses} guesses"

# Creates loop that ends when the current guess is determined to be correct
while guess != correctNum:
    try:

        # Accepts input for guess. First checks for quit command and exits program if quit
        # Detected. Otherwise attempts to convert guess to an int.
        guess = input("Guess a number from 1 to 100, or type QUIT to exit.")
        if guess in quitCommands:
            print("WHY DON'T YOU WANT TO PLAY WITH ME?")
            exit()
        else:
            guess = int(guess)

        # Raises a ValueError if "guess" is not in the proper range.
        # Technically this catches both Value and Type errors.
        if guess not in range(1, 101):
            raise ValueError
        # If no quit command was entered and the guess was legal, number of
        # guesses will iterate by one.
        else:
            numGuesses = numGuesses + 1

        # Tells user guess was either too high or too low
        # Also prints number of guesses so far
        if guess < correctNum:
            print(f"That guess was too low! {guessSoFar()} so far!")
        elif guess > correctNum:
            print(f"That guess was too high! {guessSoFar()} so far!")

    # Error message sent when ValueError is raised from in While loop above
    except ValueError:
        print("A whole number between 1 and 100, please.")

# Prints victory message with number of guesses if while loop terminates
# (That is, if the guess is correct)
print(f"YOU WIN!!! {guess} was the correct answer! It took you {guessSoFar()}!")