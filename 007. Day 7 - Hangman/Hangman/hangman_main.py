print('''
#################################################
##############      HANGMAN        ##############
#################################################
''')

import random # Imports entire random module
import hangman_art as T # Imports entire hangman_art module with alias T to call particular function
from hangman_words import word_list # Imports only the list word_list

print("Welcome to Hangman")

word_letters = []
guess_display = []
wrong_guesses = 0
flag = False

# 
def display(word_length, guess_display, chosen_word):

    count = len(chosen_word)

    print(T.tree)

    for i in word_length:

        # Print current list
        print(f"{guess_display[i]}", end=' ')

        if guess_display[i] != "_":
            count = count - 1
            if count == 0:
                print("\n\nYou Win!")
                exit()

chosen_word = random.choice(word_list)
word_length = range(len(chosen_word))
guess_letters = "_"

for i in word_length:
    word_letters.append(chosen_word[i])
    guess_display.append(guess_letters)

# Uncomment following prints to see which word was picked
# print(f"word_chosen: {chosen_word}")
# print(f"word_letters: {word_letters}")

display(word_length, guess_display, chosen_word)

# Iterate over choices
while wrong_guesses <= 6:
    user_choice = input("\nChoose guess: ")
    
    # Check each letter from randomly chosen word and flag if a letter was picked
    for i in word_length:
        if user_choice == word_letters[i].lower():
            flag = True
            guess_display[i] = word_letters[i]
            display(word_length, guess_display, chosen_word)

    # If flag is still false it means user made chose a wrong letter
    if flag == False:
        wrong_guesses = wrong_guesses + 1
        T.hangman(word_length, guess_display, wrong_guesses)

    # If we reach total number of wrong guesses, end game
    if wrong_guesses == 6:
        T.hangman(word_length, guess_display, wrong_guesses)
        print(f"\nGame Over.")
        exit()

    # Reset flag
    flag = False