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
flag = False

global tree
tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |
      |
      |
    ~~~~~'''

def hangman(word_length, guess_display, wrong_guesses): 
    global tree
    if wrong_guesses == 0:
        print({})

    elif wrong_guesses == 1:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |
      |
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 2:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |     |
      |
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 3:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |    /|
      |
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 4:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |    /|\\
      |
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 5:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |    /|\\
      |    /`
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 6:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |    /|\\
      |    /`\\
    ~~~~~'''
        print(tree)
    
    for i in word_length:
        # Print current list
        print(f"{guess_display[i]}", end=' ')

def display(word_length, guess_display, chosen_word):
    global tree
    count = len(chosen_word)

    print(tree)

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
        hangman(word_length, guess_display, wrong_guesses)

    if wrong_guesses == 6:
        hangman(word_length, guess_display, wrong_guesses)
        print(f"\nGame Over.")
        exit()

    # Reset flag
    flag = False