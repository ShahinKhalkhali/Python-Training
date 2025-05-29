###################################################
###############      HANGMAN        ###############
###################################################

import random

print("Welcome to Hangman")

word_list = ["Adieu", "Ghost", "Train", "Words", "Blame", "Topaz", "Traitorous", "Crowning", "Imagine", 
             "Planting", "Training", "Python", "Coding", "Announcement", "Phone", "Computer"]

word_letters = []
guess_display = []
wrong_guesses = 0

chosen_word = random.choice(word_list)
word_length = range(len(chosen_word))
guess_letters = "_"

for i in word_length:
    word_letters.append(chosen_word[i])
    guess_display.append(guess_letters)

print(f"word_chosen: {chosen_word}")
print(f"word_letters: {word_letters}")
print(f"guess_display: {guess_display}")

while wrong_guesses <= 5:
    user_choice = input("Choose guess: ")
    
    for i in word_length:
        print(f"Letter {i}: {word_letters[i]}")
        if user_choice == word_letters[i]:
            guess_display[i] = word_letters[i]
            print(f"guess_display: {guess_display}")
            break
        else:
            wrong_guesses = wrong_guesses + 1