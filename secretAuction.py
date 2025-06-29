#########################################################
###############      SECRET AUCTION        ##############
#########################################################

import os

auctionDict = {}
nameDict = []
bidDict = []

# def sortBids():

name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))

auctionDict[name] = bid

def main(auctionDict):
    flag = True
    i = 0
    while flag == True:
        i += i
        flag = input("Are there any other bidders? Type 'yes' or 'no'.\n")

        if flag == "yes":
            os.system('cls')
            flag = True
            name = input("What is your name?: ")
            bid = int(input("What's your bid?: $"))
            auctionDict[name] = bid

        elif flag == "no":
            print(f"Names & bids: {auctionDict}")
            #TODO: Write sorting algorith sortBids()
            exit

        else:
            flag = input("Please input either 'yes' or 'no'\n")
            main()

main(auctionDict)