print('''
#########################################################
###############      BILL SPLITTER        ###############
#########################################################
''')

print("The tip calculator\n")

bill_amount = input("Total bill: ")
tip_amount = input("\nHow much would you like to tip (10%, 15%, 20%, 25%): ")
number_people = input("\nHow many people will be splitting bill: ")

bill_amount = float(bill_amount)
tip_amount = int(tip_amount)
number_people = int(number_people)

total = (bill_amount + (bill_amount * (tip_amount/100)))/number_people
total = round(total,2)
total = str(total)

print("\nEach person will have to pay: " + total)