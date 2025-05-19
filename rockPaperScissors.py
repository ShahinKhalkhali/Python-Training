###############################################################
###############      ROCK PAPER SCISSORS        ###############
###############################################################

import random

choice_rock = 0
choice_paper = 1
choice_scissor = 2

player_choice = int(input("Welcome to the Rock Paper Scissors Game, What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
CPU_choice = random.randint(0, 2)

print("Your choice:")

if player_choice == choice_rock:
    print("""
        _______
    ---'   ____)
           (_____)
           (_____)   ROCK
           (____)
    ---.__(___)
    """)

elif player_choice == choice_paper:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)    PAPER
             _______)
    ---.__________)
    """)

elif player_choice == choice_scissor:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)    SCISSOR
          (____)
    ---.__(___)
    """)

print("CPU Choice:\n")

if CPU_choice == choice_rock:
    print("""
        _______
    ---'   ____)
           (_____)
           (_____)   ROCK
           (____)
    ---.__(___)
    """)

elif CPU_choice == choice_paper:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)    PAPER
             _______)
    ---.__________)
    """)

elif CPU_choice == choice_scissor:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)    SCISSOR
          (____)
    ---.__(___)
    """)

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