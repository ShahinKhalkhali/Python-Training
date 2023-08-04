#########################################################
###############      COFFEE MACHINE       ###############
###############        PROEJECT V1.       ###############
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

# Global Variables
profit = 0
capacityWater = 1000
capacityCoffee = 1000
capacityMilk = 1000

responseFlag = True     # ****  ADD FLAG SO THAT WE CAN DECIDE WHEN TO RESET THE LOOP (APPLICABLE   ****
                        # ****  IN ANY SITUATION BUT ANYWHERE) IN THE MAIN CODE.                    ****

# The "Resetting of the program" is explained as the following: while true, the loop will continue. 
while responseFlag:
    # When inner loop breaks 
    responseFlag = False # **** VERY IMPORTANT TO MAKE SURE THAT FLAG RESETS AFTER EACH ITERATION ****
    while (capacityWater >= 0 and capacityCoffee >= 0 and capacityMilk >= 0):

        # Reset all inputs to original values
        capacityQuarters = 0.25
        capacityDimes = 0.10
        capacityNickles = 0.05
        capacityPennies = 0.01
        capacityTotal = 0
        capacityChange = 0

        # Input
        coffeeType = input ("What would you like? (Espresso/Latte/Cappuccino): ").lower() # .lower() forces all input to be lower case.

        # Exceptions for flag to restart program                                                                                                    # TODO Review this!
        if coffeeType != "latte" and coffeeType != "espresso" and coffeeType != "cappuccino" and coffeeType != "report" and coffeeType != "off":    # "and" is the correct statement for this exception because
            print("Please enter a valid drink!")                                                                                                    # condition will never be false since coffeeType cannot be 
            responseFlag = True                                                                                                                     # 2 different strings at the same time.
            break

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
            print ("\nMoney Obtained: " + str(profit) + "$\n")
            print ("Resource Capacity")
            print ("Water left: " + str(capacityWater) + "ml")
            print ("Coffee left: " + str(capacityCoffee) + "g")
            print ("Milk left: " + str(capacityMilk) + "ml\n")
            responseFlag = True
            break

        capacityQuarters *= float(input("Insert number of Quarters: "))
        capacityDimes *= float(input("Insert number of Dimes: "))
        capacityNickles *= float(input("Insert number of Nickles: "))
        capacityPennies *= float(input("Insert number of Pennies: "))

        capacityTotal = 0
        capacityTotal = float(capacityQuarters) + float(capacityDimes) + float(capacityNickles) + float(capacityPennies)

        if (coffeeType == "espresso"):
            capacityChange = capacityTotal - 1.5
            if capacityChange <= 0:
                print("Sorry that's not enough money.")
            else:
                profit += 1.5
                print("Distributing espresso\n")
                print("Here is your change: $" + str(capacityChange))
                capacityWater -= 50
                capacityCoffee -= 18

        elif (coffeeType == "latte"):
            capacityChange = capacityTotal - 2.5
            if capacityChange <= 0:
                print("Sorry that's not enough money.")
            else:
                profit += 2.5
                print("Distributing latte\n")
                print("Here is your change: $" + str(capacityChange))
                capacityWater -= 200
                capacityCoffee -= 24
                capacityMilk -= 150

        elif (coffeeType == "cappuccino"):
            capacityChange = capacityTotal - 3.0
            if capacityChange <= 0:
                print("Sorry that's not enough money.")
            else:
                profit += 3
                print("Distributing cappuccino\n")
                print("Here is your change: $" + str(capacityChange))
                capacityWater -= 250
                capacityCoffee -= 24
                capacityMilk -= 100