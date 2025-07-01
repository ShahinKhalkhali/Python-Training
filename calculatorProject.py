print('''
#############################################################
###############      CALCULATOR PROJECT        ##############
#############################################################
''')

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

print()