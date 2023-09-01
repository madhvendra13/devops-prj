# Use the random module to help generate the random number
import random


def gameOnce():
    # randint() will generate a random integer between 1-100, assign it to 'number'
    number = random.randint(1, 100)

    # guess will store the guesses that the user makes
    guess = 0
    steps = 0
    # continue the game until the user guesses correctly
    while guess != number:

        # prompt the user to enter a guess, the input() function will return the
        # string the user enters, convert it to an int with int() and assign the
        # guess to 'guess'

        # Adding Try Catch
        try:
            guess = int(input("Enter Guess: "))
            if (guess < number):
                print("Guess higher!")
                steps += 1
            elif (guess > number):
                print("Guess lower!")
                steps += 1
            else:
                print("You won!")

        except Exception :
            print("Invalid Input.")
            return 20
    # if the user guesses too lower, tell them to guess higher, if they guess
    # too high, tell them to guess lower, and if they get it correct tell
    # them they've won

    return steps


gameNo = 0
toatalscore = 0

while (gameNo < 3):
    gameNo += 1
    sc = gameOnce()
    toatalscore += sc
    print("Game No : " + str(gameNo + 1) + "Score = " + str(sc))

print("Total Game Score : " + str(toatalscore))