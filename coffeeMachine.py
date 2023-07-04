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
capacityChange = 0

while capacityWater > 0 and capacityCoffee > 0 and capacityMilk > 0:
    # Input
    coffeeType = input ("What would you like? (Espresso/Latte/Cappuccino): ")
    capacityMoney = float(input("Insert Money: "))

    if capacityMoney >= 1.5:
        if coffeeType == "Latte":
            capacityWater -= 50
            capacityCoffee -= 18
            capacityChange = capacityMoney - 1.5
            print("Distributing latte\n")

    if capacityMoney >= 2.5:
        if coffeeType == "Espresso":
            capacityWater -= 200
            capacityCoffee -= 24
            capacityMilk -= 150
            capacityChange = capacityMoney - 2.5
            print("Distributing espresso\n")

    if capacityMoney >= 3.0:
        if coffeeType == "Cappuccino":
            capacityWater -= 250
            capacityCoffee -= 24
            capacityMilk -= 100
            capacityChange = capacityMoney - 3.0
            print("Distributing cappuccino\n")

    # Feedback
    print ("Money returned: " + str(capacityChange) + "$\n")

    print ("Resource Capacity")
    print ("Water left: " + str(capacityWater) + "ml")
    print ("Coffee left: " + str(capacityCoffee) + "g")
    print ("Milk left: " + str(capacityMilk) + "ml\n")