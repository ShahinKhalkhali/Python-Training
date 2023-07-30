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

# Variable
profit = 0

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
        for out_key, in_dict in MENU.items():
            if (out_key == "latte"):

                print(f"Outer key: {out_key}")
                for in_key, value in in_dict.items():
                    print(f"Inner key: {in_key}, Value: {value}")
                    
                    #TODO REDUCE RESOURCES
                    

    if (coffeeType == "cappuccino"):
        for out_key, in_dict in MENU.items():
            if (out_key == "cappuccino"):
                print(f"Outer key: {out_key}")
                for in_key, value in in_dict.items():
                    print(f"Inner key: {in_key}, Value: {value}")

                    #TODO REDUCE RESOURCES

    if (coffeeType == "espresso"):
        for out_key, in_dict in MENU.items():
            if (out_key == "espresso"):
                print(f"Outer key: {out_key}")
                for in_key, value in in_dict.items():
                    print(f"Inner key: {in_key}, Value: {value}")

                    #TODO REDUCE RESOURCES

while isOn:

    coffeeType = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if (coffeeType == "off"):
        isOn = False

    elif (coffeeType == "report"):
        #TODO Obtain the updated resource list
        print (f"\nMoney Obtained\nCAD: {profit}$\n")
        print ("Resource Capacity")
        print (f"Water left: {resources['water']}ml")
        print (f"Coffee left: {resources['coffee']} g")
        print (f"Milk left: {resources['milk']} ml\n")
        isOn = True

    else:
        reduceResources(coffeeType)