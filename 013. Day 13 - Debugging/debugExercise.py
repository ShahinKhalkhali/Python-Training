print('''
###########################################################
###############      DEBUG EXERCISES        ###############
###########################################################
''')

## Exercise 1

def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it")

my_function()

# ------------------------------------------------------#

## Exercise 2

from random import randint
i = True
while i == True:
    dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    dice_num = randint(0,5)
    print(dice_images[dice_num])

# ------------------------------------------------------#

## Exercise 3

i = True
while i == True:
    year = int (input("What's your year of birth?: "))
    if year >= 1980 and year < 1994:
        print("\nYou are a Millenial.")
    elif year >= 1994:
        print("\nYou are a Gen Z.")
    elif year < 1980 and year >= 1965:
            print("\nYou are a Gen X.")
    elif year < 1965:
        print("\nYou are a Baby Boomer.")

# ------------------------------------------------------#

## Exercise 4

while True:
    try:
        age = int(input("How old are you: "))
        break
    except ValueError:
        print("You have typed in an invalid number. Please try again with a numerical response.")

if age > 18:
    print(f"You can drive at age {age}")

# ------------------------------------------------------#

## Exercise 5

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)