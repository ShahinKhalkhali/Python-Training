#########################################################
###############      COFFEE MACHINE       ###############
###############         PROEJECT          ###############
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

# Variables
capacityWater = 1000
capacityCoffee = 1000
capacityMilk = 1000
capacityMoney = 0

# Input
coffeeType = input ("What would you like? (Espresso/Latte/Cappuccino): ")
capacityMoney = float(input("Insert Money: "))

#TODO ADD LOOP CONDITION WHILE WATER/MILK/COFFEE/MONEY MEETS CONDITIONS

while capacityWater > 0 and capacityCoffee > 0 and capacityMilk > 0:

    if capacityMoney >= 1.5:
        if coffeeType == "Latte":
            print("Distributing latte")
            #TODO REMOVE RESOURCE FROM MACHINE FUNCTION


    if capacityMoney >= 2.5:
        if coffeeType == "Espresso":
            print("Distributing espresso")
            #TODO REMOVE RESOURCE FROM MACHINE FUNCTION


    if capacityMoney >= 3.0:
        if coffeeType == "Cappuccino":
            print("Distributing cappuccino")
            #TODO REMOVE RESOURCE FROM MACHINE FUNCTION