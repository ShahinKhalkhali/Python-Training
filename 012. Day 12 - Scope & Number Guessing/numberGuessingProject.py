print('''
###########################################################
###############      GUESS THE NUMBER        ##############
###########################################################
''')

import random

randNumber = int(random.randint(0,100))

def compare_guess(randNumber, difficulty, flag):
    numberChosen = int(input("Choose a number to guess: "))
    print(f"numberChosen: {numberChosen}\nrandNumber: {randNumber}")
    if difficulty.lower() == "hard":
        while flag < 6:
            if numberChosen > randNumber:
                print(f"Number is too high")
                flag += 1
                compare_guess(randNumber, difficulty, flag)
            elif numberChosen < randNumber:
                print(f"Number is too low")
                flag += 1
                compare_guess(randNumber, difficulty, flag)
            elif numberChosen == randNumber:
                print(f"You guessed the right number!")
                play_again()

        print("You have no more guesses.\n")
        play_again()

    elif difficulty.lower() == "easy":
        while flag < 11:
            if numberChosen > randNumber:
                print(f"Number is too high")
                flag += 1
                compare_guess(randNumber, difficulty, flag)
            elif numberChosen < randNumber:
                print(f"Number is too low")
                flag += 1
                compare_guess(randNumber, difficulty, flag)
            elif numberChosen == randNumber:
                print(f"You guessed the right number!")
                play_again()

        print("\nYou ran out of guesses! :()")
        play_again()

def play_again():
    while True:
        replay = input("\nDo you want to play another game of Blackjack? Type 'Y' or 'N': ")
        if replay.lower() == 'y':
            main()
        elif replay.lower() == 'n':
            exit()
        else:
            print("\nPlease enter a valid input.")

def main():
    flag = 0
    difficulty = input("Choose a difficulty (Hard or Easy): ")
    compare_guess(randNumber, difficulty, flag)

main()