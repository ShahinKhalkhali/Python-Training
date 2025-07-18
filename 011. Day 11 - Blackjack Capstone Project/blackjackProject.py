print('''
############################################################
###############      BLACKJACK PROJECT        ##############
############################################################''')

import random

# 1- TODO: Create flowchart
# 2- TODO: Create dynamic dictionary for player & bot

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = [random.choice(cards), random.choice(cards)]
computer_hand = [random.choice(cards)]
player_hand_sum = sum(player_hand)
computer_hand_sum = sum(computer_hand)

def hit_stand_function(player_hand, player_hand_sum):

    hit_stand = input("Type 'H' to Hit or 'S' to Stand: ")

    if hit_stand.lower() == 'h':
        print("\nHit!")
        player_hand.insert(0, random.choice(cards))
        player_hand_sum = sum(player_hand)

        if player_hand_sum > 21:    # Condition that if the number if '11' replace it with '1'
            if 11 in player_hand:
                ace_index = player_hand.index(11)
                player_hand[ace_index] = 1
                player_hand_sum = sum(player_hand)
                print_score(player_hand, computer_hand, player_hand_sum, computer_hand_sum)
                return player_hand, player_hand_sum
            
            player_hand_sum = sum(player_hand)
            print_score(player_hand, computer_hand, player_hand_sum, computer_hand_sum)
            print(f"\nBust, your score is {player_hand_sum}! Better luck next time :(")
            play_again(player_hand_sum, computer_hand_sum)

        elif player_hand_sum < 21:
            print_score(player_hand, computer_hand, player_hand_sum, computer_hand_sum)
        
        else:
            print("Blackjack!")
            print_score(player_hand, computer_hand, player_hand_sum, computer_hand_sum)
            computer_function(player_hand, computer_hand, player_hand_sum, computer_hand_sum)
        
    elif hit_stand.lower() == 's':
        print("\nStand!")
        player_hand_sum = sum(player_hand)
        computer_function(player_hand, computer_hand, player_hand_sum, computer_hand_sum)
        play_again(player_hand_sum, computer_hand_sum)

    else:
        print("\nPlease insert a valid input.")
        hit_stand_function()

def computer_function(player_hand, computer_hand, player_hand_sum, computer_hand_sum):
    flag = True
    while flag == True:

        print_score(player_hand, computer_hand, player_hand_sum, computer_hand_sum)
        
        if computer_hand_sum > 21:
            if 11 in computer_hand:
                ace_index = computer_hand.index(11)
                computer_hand[ace_index] = 1
                computer_hand_sum = sum(computer_hand)
                return computer_hand, computer_hand_sum
            computer_hand_sum = sum(computer_hand)
            play_again(player_hand_sum, computer_hand_sum)

        elif computer_hand_sum > 16:
            computer_hand_sum = sum(computer_hand)
            play_again(player_hand_sum, computer_hand_sum)

        elif computer_hand_sum < 21:
            computer_hand.insert(0, random.choice(cards))
            computer_hand_sum = sum(computer_hand)

def play_again(player_hand_sum, computer_hand_sum):

    win_condition(player_hand_sum, computer_hand_sum)

    replay = input("\nDo you want to play another game of Blackjack? Type 'Y' or 'N': ")

    if replay.lower() == 'y':
        player_hand = [random.choice(cards), random.choice(cards)]
        computer_hand = [random.choice(cards)]
        player_hand_sum = sum(player_hand)
        main(player_hand, computer_hand, player_hand_sum, computer_hand_sum)
    
    else:
        exit()

def print_score(player_hand, computer_hand, player_hand_sum, computer_hand_sum):
    print(f"\nYour cards: {player_hand}, current score: {player_hand_sum}")
    print(f"Computer's cards: {computer_hand}, computer's score: {computer_hand_sum}")

def win_condition(player_hand_sum, computer_hand_sum):
    if player_hand_sum < 22 and computer_hand_sum < 22 and computer_hand_sum > player_hand_sum:
        print(f"\nComputer Wins with {computer_hand_sum}! Better luck next time :(")
    elif player_hand_sum < 22 and computer_hand_sum < 22 and computer_hand_sum < player_hand_sum:
        print(f"\nPlayer Wins with {player_hand_sum}! Congratulations :D")
    elif player_hand_sum == computer_hand_sum:
        print(f"\nDraw, both player & dealer {player_hand_sum} == {computer_hand_sum}")
    elif player_hand_sum > 21:
        return
    else:
        print(f"\nDealer bust with {computer_hand_sum}, Congrats you win with {player_hand_sum}")

def main(player_hand, computer_hand, player_hand_sum, computer_hand_sum):

    print(f"\nYour cards: {player_hand}, current score: {player_hand_sum}")
    print(f"Computer's first card: {computer_hand}")

    flag = True

    while flag == True:

        if player_hand_sum == 21:
            print(f"\nYou got Black Jack!")
            computer_function(player_hand, computer_hand, player_hand_sum, computer_hand_sum)
            play_again(player_hand_sum, computer_hand_sum)
            
        hit_stand_function(player_hand, player_hand_sum)

main(player_hand, computer_hand, player_hand_sum, computer_hand_sum)