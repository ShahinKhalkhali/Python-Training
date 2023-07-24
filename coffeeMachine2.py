#########################################################
###############      COFFEE MACHINE       ###############
###############        PROEJECT V2.       ###############
#########################################################

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

def reduceResources(coffeeType):

    if (coffeeType == "latte"):
        print("Reducing latte resources")
        for item in MENU.get('latte').get('ingredients'):
            #TODO Figure out how to obtain values


while isOn:
    
    coffeeType = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if (coffeeType == "off"):
        isOn = False

    elif (coffeeType == "report"):
            #TODO Obtain the updated resource list
            print ("\nMoney Obtained: " + str(capacityTotal) + "$\n")
            print ("Resource Capacity")
            print ("Water left: " + str(capacityWater) + "ml")
            print ("Coffee left: " + str(capacityCoffee) + "g")
            print ("Milk left: " + str(capacityMilk) + "ml\n")
            isOn = True
            break

    else:
        reduceResources(coffeeType)