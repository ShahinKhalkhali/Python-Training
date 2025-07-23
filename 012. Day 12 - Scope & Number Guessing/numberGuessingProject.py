print('''
###########################################################
###############      GUESS THE NUMBER        ##############
###########################################################
''')

import random

randNumber = random.randint(0,100)

def compareGuess(numberChosen, randNumber):
    print(f"numberChosen: {numberChosen}\nrandNumber: {randNumber}")
    if difficulty == "hard":
        while flag < 6:
            if numberChosen > randNumber:
                print(f"Number is too high")
                flag += 1
            elif numberChosen < randNumber:
                print(f"Number is too low")
                flag += 1
            elif numberChosen == randNumber:
                print(f"You guessed the right number!")
                
    elif difficulty == "easy":
        while flag < 11:
            if numberChosen > randNumber:
                print(f"Number is too high")
                flag += 1
            elif numberChosen < randNumber:
                print(f"Number is too low")
                flag += 1
            elif numberChosen == randNumber:
                print(f"You guessed the right number!")

def main():
    numberChosen = input("Choose a number to guess: ")
    compareGuess(numberChosen, randNumber)

main()