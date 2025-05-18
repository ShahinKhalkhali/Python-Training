############################################################
###############       PYTHON TRAINING        ###############
###############         By SHAHIN K.         ###############
############################################################

## Example 1 (Printing)
# Outputting
print ("Day 1 - Python Print Function\nThe function is declared like this\nprint('what to print')\n") # New line
print ("Hello" + " " + "World") # Concatenation

# Inputting
x = input ("Write your name: ") # print instruction and ask user to input string
print ("You Entered: ", x)

## Example 2 (f-strings)
days = 365
print (f"There are {days} in a year")

## Example 3 (Type check)
integer = 123
string = "abc"
floating = 123.456

print(type(integer), type(string), type(floating))

## Example 4 (Fix w/ type casting)
print("Number of letters in your name: " + str(int(len(input("Enter your name: ")))))

## Example 5 (Types of operators --> PEMDAS)
print("123")        # Concatenation
print(123 + 456)    # Addition
print(2 * 3)        # Multiplication
print(6 / 2)        # Division (float)
print(6 // 2)       # Division (integer)
print(2 ** 5)       # Exponetial

## Example 6 (Even/Odd Modulo)
number_input = int(input("Is this number even or odd: "))
number_check = number_input % 2
if number_check == 0:
    print("\nThis number is even")
else:
    print("\nThis number is odd")