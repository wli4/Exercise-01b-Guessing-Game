import sys
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"
number = 5
guess = input("Guess a number from 1 to 10: ")

if guess not in ['1' ,'2','3', '4', '5', '6', '7', '8', '9', '10']:
    raise ValueError("Please limit the guess to a number from 1 to 10.")

guess = int(guess)
if guess == number:
    print("Great job! You got it!")
else:
    print("Sorry, better luck next time.")
    print("The number was " + str(number))