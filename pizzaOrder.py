#######################################################
###############      PIZZA ORDER        ###############
#######################################################

print("Welcome to Pizza-Hut may I take your order")
pizza_size = input("\nLarge/Medium/Small: ")
pizza_pepperoni = input("\nDo you want pepperoni (y/n): ")
pizza_extra_cheese = input("\nDo you want extra cheese (y/n): ")

pizza_bill = 0

if pizza_size == "Large" or 'L' or 'l':
    pizza_bill += 25
elif pizza_size == "Medium" or 'M' or 'm':
    pizza_bill += 20
elif pizza_size == "Small" or 'S' or 's':
    pizza_bill += 15

if pizza_pepperoni == 'y':
    if pizza_size == "Large" or "L" or 'l' or "Medium" or 'M' or 'm':
        pizza_bill += 3
    elif pizza_size == "Small" or 'S' or 's':
        pizza_bill += 1

if pizza_extra_cheese == 'y':
    pizza_bill += 1

print(f"\nYour total bill is ${pizza_bill}.")