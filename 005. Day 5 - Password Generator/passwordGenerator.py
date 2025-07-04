print('''
##############################################################
###############      PASSWORD GENERATOR        ###############
##############################################################
''')

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

length_letter = range(0, nr_letters)
length_symbol = range(0, nr_symbols)
length_number = range(0, nr_numbers)

# Easy Level (Order of letter/symbols/numbers is fixed)

part_letter = ""
part_symbol = ""
part_number = ""

for i in length_letter:
    part_letter += str(letters[random.randint(0, 25)])

for i in length_symbol:
    part_symbol += str(symbols[random.randint(0, 8)])

for i in length_number:
    part_number += str(numbers[random.randint(0, 9)])

print(f"\nEasy password (in order): {part_letter}{part_symbol}{part_number}")

# Hard Level (Order of letter/symbols/numbers is random)

hardpass = ""
pass_list = []

for i in length_letter:
    pass_list.append(random.choice(letters))

for i in length_symbol:
    pass_list.append(random.choice(symbols))

for i in length_number:
    pass_list.append(random.choice(numbers))

random.shuffle(pass_list)

for i in range(len(pass_list)):
    hardpass += str(pass_list[i])

print(f"\nHard password (in random order): {hardpass}")