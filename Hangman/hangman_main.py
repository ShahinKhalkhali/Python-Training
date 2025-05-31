###################################################
###############      HANGMAN        ###############
###################################################

import random
import hangman_words as WL
import hangman_art as T

print("Welcome to Hangman")

from hangman_words import word_list
from hangman_art import tree

word_letters = []
guess_display = []
wrong_guesses = 0
flag = False

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

# print(f"word_chosen: {chosen_word}")
# print(f"word_letters: {word_letters}")
# print(f"guess_display: {guess_display}")

display(word_length, guess_display, chosen_word)

while wrong_guesses <= 6:
    user_choice = input("\nChoose guess: ")
    
    for i in word_length:
        # print(f"Letter {i}: {word_letters[i]}")
        if user_choice == word_letters[i].lower():
            flag = True
            guess_display[i] = word_letters[i]
            # print(f"guess_display: {guess_display}")
            display(word_length, guess_display, chosen_word)

    if flag == False:
        wrong_guesses = wrong_guesses + 1
        T.hangman(word_length, guess_display, wrong_guesses)

    if wrong_guesses == 6:
        T.hangman(word_length, guess_display, wrong_guesses)
        print(f"\nGame Over.")
        exit()

    # Reset flag
    flag = False