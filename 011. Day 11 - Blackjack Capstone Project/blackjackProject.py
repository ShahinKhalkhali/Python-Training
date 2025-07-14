print('''
############################################################
###############      BLACKJACK PROJECT        ##############
############################################################
''')

import random

# 1- TODO: Create flowchart
# 2- TODO: Create dynamic dictionary for player & bot

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = [random.choice(cards), random.choice(cards)]
computer_hand = [random.choice(cards)]
player_hand_sum = player_hand[0] + player_hand[1]

flag = True

def hit_stand_function():

    hit_stand = input("Type 'H' to Hit or 'S' to Stand: ")

    if hit_stand.lower() == 'h':
        # TODO: Insert function for hit
        print("Hit!")
        player_hand.insert(1, random.choice(cards))
        if player_hand_sum > 21:
            print(f"Bust, your score is {player_hand_sum}! Better luck next time :(")
            play_again()
        elif player_hand_sum < 21:
            print(f"Your score is {player_hand_sum}")
            return player_hand

    elif hit_stand.lower() == 's':
        # TODO: Insert function for stand
        print("Stand!")

    else:
        print("\nPlease insert a valid input.")
        hit_stand_function()

def play_again():
    replay = input("Do you want to play another game of Blackjack? Type 'Y' or 'N': ")

    if replay.lower() == 'y':
        main()
    
    else:
        exit()

def main():

    while flag == True:
        print(f"Your cards: {player_hand}, current score: {player_hand_sum}")
        print(f"Computer's first card: {computer_hand}")
        
        if player_hand_sum == 21:
            print(f"You got Black Jack!")
            # TODO: Insert function for computer's play

        hit_stand_function()
        player_hand_sum = sum()