#########################################################
###############      COFFEE MACHINE       ###############
###############         PROEJECT          ###############
#########################################################

# Espresso      --> Requires:   50ml Water 
#                               18g Coffee

# Latte         --> Requires:   200ml Water 
#                               24g Coffee
#                               150ml Milk

# Cappuccino    --> Requires:   250ml Water 
#                               24g Coffee
#                               100ml Milk

coffeeType = input ("What would you like? (Espresso/Latte/Cappuccino): ")

#TODO ADD LOOP CONDITION UNTIL WATER/MILK/COFFEE/MONEY MEETS CONDITIONS

if coffeeType == "Latte":
    print("Distributing latte")
    #TODO REMOVE RESOURCE FROM MACHINE

if coffeeType == "Espresso":
    print("Distributing espresso")
    #TODO REMOVE RESOURCE FROM MACHINE

if coffeeType == "Cappuccino":
    print("Distributing cappuccino")
    #TODO REMOVE RESOURCE FROM MACHINE