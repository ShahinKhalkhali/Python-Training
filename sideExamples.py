############################################################
###############       PYTHON TRAINING        ###############
###############         By SHAHIN K.         ###############
############################################################

import random

# ## Example 1 (Printing)
# # Outputting
# print ("Day 1 - Python Print Function\nThe function is declared like this\nprint('what to print')\n") # New line
# print ("Hello" + " " + "World") # Concatenation

# # Inputting
# x = input ("Write your name: ") # print instruction and ask user to input string
# print ("You Entered: ", x)

# ## Example 2 (f-strings)
# days = 365
# print (f"There are {days} in a year")

# ## Example 3 (Type check)
# integer = 123
# string = "abc"
# floating = 123.456

# print(type(integer), type(string), type(floating))

# ## Example 4 (Fix w/ type casting)
# print("Number of letters in your name: " + str(int(len(input("Enter your name: ")))))

# ## Example 5 (Types of operators --> PEMDAS)
# print("123")        # Concatenation
# print(123 + 456)    # Addition
# print(2 * 3)        # Multiplication
# print(6 / 2)        # Division (float)
# print(6 // 2)       # Division (integer)
# print(2 ** 5)       # Exponetial

# ## Example 6 (Even/Odd Modulo)
# number_input = int(input("Is this number even or odd: "))
# number_check = number_input % 2
# if number_check == 0:
#     print("\nThis number is even")
# else:
#     print("\nThis number is odd")

# ## Example 7 (Random coin flip)
# random_integer = random.randint(1, 10)
# print("Random number is: " + str(random_integer) + "\n")
# coin_toss = random_integer % 2
# if coin_toss == 0:
#     print("Coin is flipped... Heads!")
# else:
#     print("Coin is flipped... Tails!")

# ## Example 8 (High score)

# student_scores = [180, 124, 165, 173, 189, 169, 146, 199]
# list_size = range(len(student_scores))
# temp1 = 0
# temp2 = 0
# # Range method
# for i in list_size:
#     if i == 0:
#         temp1 = student_scores[i]
#         i += 1
#     else:
#         if temp1 < student_scores[i]:
#             temp1 = student_scores[i]
#             i += 1

# # Simple method
# for i in student_scores:
#     if i > temp2:
#         temp2 = i

# print(f"This is the highest score using range() method: {temp1}")
# print(f"This is the highest score using simple method: {temp2}")

# ## Example 9 (Gauss' Challenge)

# list_100 = range(1, 101)
# gauss_100 = 0
# temp = 0

# size_list = int((len(list_100))/2)

# print(f"list_100 size: {size_list}")

# for i in range(size_list):
#     temp = list_100[i] + list_100[-i - 1]
#     gauss_100 += temp

# print(f"The Gauss output is: {gauss_100}")

# ## Example 10 (FizzBuzz)

# word = ["Fizz", "Buzz", "FizzBuzz"]
# numbers = range(1, 101)

# for i in numbers:

#     if (i % 3) == 0 and (i % 5) == 0:
#         print(f"{word[2]}")
#     elif (i % 3) == 0:
#         print(f"{word[0]}")
#     elif (i % 5) == 0:
#         print(f"{word[1]}")
#     else:
#         print(f"{i}")
