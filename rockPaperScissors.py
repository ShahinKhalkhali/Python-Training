###############################################################
###############      ROCK PAPER SCISSORS        ###############
###############################################################

import random

choice_rock ='''
        _______
    ---'   ____)
           (_____)
           (_____)   ROCK
           (____)
    ---.__(___)
'''

choice_paper ='''
         _______
    ---'    ____)____
               ______)
              _______)    PAPER
             _______)
    ---.__________)
'''

choice_scissor = '''
        _______
    ---'   ____)____
              ______)
           __________)    SCISSOR
          (____)
    ---.__(___)
'''

game_images = [choice_rock, choice_paper, choice_scissor]

player_choice = int(input("Welcome to the Rock Paper Scissors Game, What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
CPU_choice = random.randint(0, 2)

# Catch error
while player_choice < 0 or player_choice > 2:
        player_choice = int(input("\nYou have chosen an invalid number, please type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

print("Your choice:")

if player_choice == 0:
    print(game_images[0])

elif player_choice == 1:
    print(game_images[1])

elif player_choice == 2:
    print(game_images[2])

print("CPU Choice:\n")

if CPU_choice == 0:
    print(game_images[0])

elif CPU_choice == 1:
    print(game_images[1])

elif CPU_choice == 2:
    print(game_images[2])

if player_choice == 0 and CPU_choice == 1:
    print("\nYOU LOST!")
elif player_choice == 0 and CPU_choice == 2:
    print("\nYOU WON!")
elif player_choice == 1 and CPU_choice == 0:
    print("\nYOU WON!")
elif player_choice == 1 and CPU_choice == 2:
    print("\nYOU LOST!")
elif player_choice == 2 and CPU_choice == 0:
    print("\nYOU LOST!")
elif player_choice == 2 and CPU_choice == 1:
    print("\nYOU WON!")
elif player_choice == 0 and CPU_choice == 0:
    print("\nDRAW!")
elif player_choice == 0 and CPU_choice == 0:
    print("\nDRAW!")
elif player_choice == 0 and CPU_choice == 0:
    print("\nDRAW!")