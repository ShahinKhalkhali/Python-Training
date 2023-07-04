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
capacityQuarters = 0
capacityDimes = 0
capacityNickles = 0
capacityPennies = 0
capacityTotal = 0
capacityChange = 0

while capacityWater >= 0 and capacityCoffee >= 0 and capacityMilk >= 0:
    # Input
    coffeeType = input ("What would you like? (Espresso/Latte/Cappuccino): ")
    capacityQuarters = float(input("Insert Quarters: "))
    capacityDimes = float(input("Insert Dimes: "))
    capacityNickles = float(input("Insert Nickles: "))
    capacityPennies = float(input("Insert Pennies: "))

    capacityTotal = float(capacityQuarters) + float(capacityDimes) + float(capacityNickles) + float(capacityPennies)

    if capacityTotal >= 1.5:
        if coffeeType == "Latte":
            capacityWater -= 50
            capacityCoffee -= 18
            capacityChange = capacityTotal - 1.5
            print("Distributing latte\n")

    if capacityTotal >= 2.5:
        if coffeeType == "Espresso":
            capacityWater -= 200
            capacityCoffee -= 24
            capacityMilk -= 150
            capacityChange = capacityMoney - 2.5
            print("Distributing espresso\n")

    if capacityTotal >= 3.0:
        if coffeeType == "Cappuccino":
            capacityWater -= 250
            capacityCoffee -= 24
            capacityMilk -= 100
            capacityChange = capacityMoney - 3.0
            print("Distributing cappuccino\n")

    if capacityWater <= 0:
        print("Sorry there is not enough water.")
    
    if capacityCoffee <= 0:
        print("Sorry there is not enough coffee.")

    if capacityMilk <= 0:
        print("Sorry there is not enough milk.")

    # Feedback
    print ("Money returned: " + str(capacityChange) + "$\n")

    print ("Resource Capacity")
    print ("Water left: " + str(capacityWater) + "ml")
    print ("Coffee left: " + str(capacityCoffee) + "g")
    print ("Milk left: " + str(capacityMilk) + "ml\n")
