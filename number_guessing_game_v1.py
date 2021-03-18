"""A Python number guessing game that implements lists, random module, control flow."""

import random
from replit import clear

# Variables
listNumbers = []

# Returns a random number from a g iven list
def returnRandomNumber(listNumbers):
    return random.choice(listNumbers)

# Welcomes user to game
def welcomeUser():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1-100.")

# Add the numbers 0 - 100 into a list
def populateList(listNumbers):
    for i in range(1, 101):
        listNumbers.append(i)
    return listNumbers

# Prompts user to choose difficulty and returns number of guesses
def selectDifficulty():
    strUserDifficulty = ''
    while (strUserDifficulty != 'easy' and strUserDifficulty != 'hard'):
        strUserDifficulty = input(
            "Choose a difficulty. Type 'easy' or 'hard': ")
    if strUserDifficulty == 'easy':
        return 10
    else:  # 'hard'
        return 5

# Prompts user to guess number and returs the number guessed
def guessNumber():
    return int(input("Make a guess: "))

# Checks the guess of the user to that of the correct guess and returns boolean
# True if user wins False otherwise
def checkGuess(userGuess, correctGuess):
    if userGuess > correctGuess:
        print(f"{userGuess} is too high.\nGuess Again.")
        return False
    elif userGuess < correctGuess:
        print(f"{userGuess} is too low.\nGuess Again.")
        return False
    else:
        print(f"Correct! The correct number was {correctGuess}.")
        return True

# Shows user how many guesses they have left
def showNumOfGuessesLeft(intNumGuesses):
    print(f"You have {intNumGuesses} guesses left.")

# Asks user if they want to play again and returns a boolean
def playAgain():
    playAgain = ''
    while (playAgain != "yes" and playAgain != "no"):
        playAgain = input("Do you want to play again? 'yes' or 'no': ")
    if (playAgain == "yes"):
        clear()
        return True
    else:
        clear()
        return False

# Game Loop
boolPlayAgain = True

while (boolPlayAgain == True):
    welcomeUser()
    listNumbers = populateList(listNumbers)
    intRandomNumber = returnRandomNumber(listNumbers)
    print(f"PSST the correct number is {intRandomNumber}")
    intNumberOfGuesses = selectDifficulty()
    boolGuessFound = False
    clear() 

    while (intNumberOfGuesses > 0 and boolGuessFound == False):
        showNumOfGuessesLeft(intNumberOfGuesses)
        userGuess = guessNumber()
        clear()
        boolGuessFound = checkGuess(userGuess, intRandomNumber)
        if boolGuessFound == False:
            intNumberOfGuesses -= 1
    if (boolGuessFound == False):
        print(f"Sorry you lose. The correct number was {intRandomNumber}.")
    boolPlayAgain = playAgain() 

# Goodbye 
print("See you next time!")
