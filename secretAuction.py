#########################################################
###############      SECRET AUCTION        ##############
#########################################################

import os

auctionDict = {}
nameDict = []
bidDict = []

def sortBids():

    highestBid = 0

    for name, bid in auctionDict.items():
        if bid > highestBid:
            highestBid = bid
            winner = name
    
    print(f"\nThe winner is {winner} with a bid of ${highestBid}")

name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))

auctionDict[name] = bid

def main(auctionDict):
    flag = True
    while flag == True:
        flag = input("Are there any other bidders? Type 'yes' or 'no'.\n")

        if flag == "yes":
            os.system('cls')
            flag = True
            name = input("What is your name?: ")
            bid = int(input("What's your bid?: $"))
            auctionDict[name] = bid

        elif flag == "no":
            sortBids()
            exit()

        else:
            flag = input("Please input either 'yes' or 'no'\n")
            main()

main(auctionDict)