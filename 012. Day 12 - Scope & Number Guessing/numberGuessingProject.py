import random

randNumber = int(random.randint(1,100))

def compare_guess(randNumber, flag):

    difficulty = input("Choose a difficulty (Hard or Easy): ")

    if difficulty.lower() == "hard":
        while flag < 6:
            numberChosen = int(input("Choose a number to guess: "))
            print(f"numberChosen: {numberChosen}")
            if numberChosen > randNumber:
                print(f"Number is too high\n")
                flag += 1
            elif numberChosen < randNumber:
                print(f"Number is too low\n")
                flag += 1
            elif numberChosen == randNumber:
                print(f"You guessed the right number!\n")
                play_again()
        print("You have no more guesses.\n")
        play_again()

    elif difficulty.lower() == "easy":
        while flag < 11:
            numberChosen = int(input("Choose a number to guess: "))
            print(f"numberChosen: {numberChosen}") # Print randNumber here if you want to see 
            if numberChosen > randNumber:
                print(f"Number is too high\n")
                flag += 1
            elif numberChosen < randNumber:
                print(f"Number is too low\n")
                flag += 1
            elif numberChosen == randNumber:
                print(f"You guessed the right number!\n")
                play_again()
        print("\nYou ran out of guesses! :(")
        play_again()

    else:
        print("Please input a valid difficulty.\n")
        compare_guess(randNumber, flag)

def play_again():
    while True:
        replay = input("\nDo you want to play another game of Blackjack? Type 'Y' or 'N': ")
        if replay.lower() == 'y':
            randNumber = int(random.randint(1,100))
            main(randNumber)
        elif replay.lower() == 'n':
            exit()
        else:
            print("\nPlease enter a valid input.")

def main(randNumber):

    print('''
###########################################################
###############      GUESS THE NUMBER        ##############
###########################################################
    ''')

    flag = 0
    compare_guess(randNumber, flag)

main(randNumber)