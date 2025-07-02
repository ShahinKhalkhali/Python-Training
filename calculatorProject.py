print('''
#############################################################
###############      CALCULATOR PROJECT        ##############
#############################################################
''')

import os

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - substract, multiply, and divide.
def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
calculatorDict = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# TODO: Create calculator

def main():

    # TODO: Add docString

    initialNumber = int(input("What's the first number?: "))

    flag = True

    while flag == True:

        for key in calculatorDict:
            print(key)

        operator = input("Pick an operation: ")

        nextNumber = int(input("What's the next number?: "))
        output = calculatorDict[operator](initialNumber, nextNumber)
        print(f"{initialNumber} {operator} {nextNumber} = {output}")
        
        choice = input(f"\nType 'y' to continue calculating with {output}, or Type 'n' to start a new calculation: ")

        if choice == "y".lower():
            print(f"\n------ Previous Value: {output} ------ \n")
            flag = True
            initialNumber = output

        else:
            os.system('cls')
            print('''
#############################################################
###############      CALCULATOR PROJECT        ##############
#############################################################
''')
            main()

main()
