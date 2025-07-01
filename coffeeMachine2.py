print('''
#########################################################
###############      COFFEE MACHINE       ###############
###############        PROEJECT V2.       ###############
#########################################################
''')

# Espresso      --> Requires:   50ml Water 
#                               18g Coffee
#                               1.50 $

# Latte         --> Requires:   200ml Water 
#                               24g Coffee
#                               150ml Milk
#                               2.50 $

# Cappuccino    --> Requires:   250ml Water 
#                               24g Coffee
#                               100ml Milk
#                               3.00 $

# Initialize Variables
moneyCost = 0
profit = 0
totalCapacity = 0
capacityChange = 0
coffeeType = "N/A"

# Dictionnary for menu of coffees
MENU = {                            # To call a key from the dictionnary you need to call the MENU Dictionnary
    "espresso": {                   # and access the key. 
        "ingredients": {            # 
            "water": 50,            # For example: print(MENU["espresso"]) --> This will list the MENU dictionnary in an array
            "coffee": 18,           # (To access all keys and their values include for loop of key and print their names and values)
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
}

isOn = True

def addMoney(coffeeType):

    global profit

    moneyCost = str(MENU[coffeeType]['cost'])

    # Reset values
    quartersCapacity = 0.25
    dimesCapacity = 0.10
    nicklesCapacity = 0.05
    penniesCapacity = 0.01
    totalCapacity = 0
    capacityChange = 0

    print("For your " + coffeeType + ", please insert $" + moneyCost)
    quartersCapacity *= float(input("Number of Quarters: "))
    dimesCapacity *= float(input("Number of Dimes: "))
    nicklesCapacity *= float(input("Number of Nickles: "))
    penniesCapacity *= float(input("Number of Pennies: "))
    totalCapacity = float(quartersCapacity) + float(dimesCapacity) + float(nicklesCapacity) + float(penniesCapacity)

    if (coffeeType == "latte"):
        capacityChange = totalCapacity - float(moneyCost)
        if capacityChange <= 0:
            print("Sorry that's not enough money.")
        else:
            profit += 2.5
            print("Distributing " + coffeeType)
            print("Here is your change: " + str(capacityChange))
            return profit

    if (coffeeType == "cappuccino"):
        capacityChange = totalCapacity - float(moneyCost)
        if capacityChange <= 0:
            print("Sorry that's not enough money.")
        else:
            profit += 3.0
            print("Distributing " + coffeeType)
            print("Here is your change: " + str(capacityChange))
            return profit

    if (coffeeType == "espresso"):
        capacityChange = totalCapacity - float(moneyCost)
        if capacityChange <= 0:
            print("Sorry that's not enough money.")
        else:
            profit += 1.5
            print("Distributing " + coffeeType)
            print("Here is your change: " + str(capacityChange))
            return profit


def reduceResources(coffeeType):
    # Check if the coffeeType exists in the MENU
    if coffeeType in MENU:
        # Iterate over the ingredients of the coffeeType
        for ingredient, amount in MENU[coffeeType]['ingredients'].items():
            # Check if there is enough of each ingredient in totalResources
            if resources[ingredient] >= amount:
                resources[ingredient] -= amount
            else:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True
    else:
        print(f"Sorry, we do not serve {coffeeType}.")
        return False

while isOn:

    coffeeType = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if (coffeeType == "off"):
        isOn = False

    elif (coffeeType == "report"):
        #TODO Obtain the updated resource list
        print (f"\nMoney Obtained\nCAD: " + str(profit) + "$\n")
        print ("Resource Capacity")
        print (f"Water left: {resources['water']}ml")
        print (f"Coffee left: {resources['coffee']} g")
        print (f"Milk left: {resources['milk']} ml\n")
        isOn = True

    else:
        addMoney(coffeeType)
        reduceResources(coffeeType)