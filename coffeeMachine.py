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
capacityQuarters = 0.25
capacityDimes = 0.10
capacityNickles = 0.05
capacityPennies = 0.01
capacityTotal = 0
capacityChange = 0

while capacityWater >= 0 and capacityCoffee >= 0 and capacityMilk >= 0:
    # Input
    coffeeType = input ("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    # Machine Resource Notice
    if capacityWater <= 0:
        print("Sorry there is not enough water.")
        quit()
    
    if capacityCoffee <= 0:
        print("Sorry there is not enough coffee.")
        quit()

    if capacityMilk <= 0:
        print("Sorry there is not enough milk.")
        quit()

    if coffeeType == "off":
        print("Coffee machine will now turn off.")
        quit()

    elif coffeeType == "report":
    # Feedback Report
        print ("\nMoney Obtained: " + str(capacityTotal) + "$\n")
        print ("Resource Capacity")
        print ("Water left: " + str(capacityWater) + "ml")
        print ("Coffee left: " + str(capacityCoffee) + "g")
        print ("Milk left: " + str(capacityMilk) + "ml\n")

    capacityQuarters *= int(input("Insert number of Quarters: "))
    capacityDimes *= int(input("Insert number of Dimes: "))
    capacityNickles *= int(input("Insert number of Nickles: "))
    capacityPennies *= int(input("Insert number of Pennies: "))

    capacityTotal = int(capacityQuarters) + int(capacityDimes) + int(capacityNickles) + int(capacityPennies)

    if (coffeeType == "latte"):
        capacityChange = capacityTotal - 1.5
        if capacityChange <= 0:
            print("Sorry that's not enough money.")
        else:
            print("Distributing latte\n")
            print("Here is your change: $" + str(capacityChange))
            capacityWater -= 50
            capacityCoffee -= 18

    elif (coffeeType == "espresso"):
        capacityChange = capacityTotal - 2.5
        if capacityChange <= 0:
            print("Sorry that's not enough money.")
        else:
            print("Distributing espresso\n")
            print("Here is your change: $" + str(capacityChange))
            capacityWater -= 200
            capacityCoffee -= 24
            capacityMilk -= 150

    elif (coffeeType == "cappuccino"):
        capacityChange = capacityTotal - 3.0
        if capacityChange <= 0:
            print("Sorry that's not enough money.")
        else:
            print("Distributing cappuccino\n")
            print("Here is your change: $" + str(capacityChange))
            capacityWater -= 250
            capacityCoffee -= 24
            capacityMilk -= 100