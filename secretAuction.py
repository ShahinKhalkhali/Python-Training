#########################################################
###############      SECRET AUCTION        ##############
#########################################################

import os

auctionDict = {}

def sortBids(auctionDict):

    highestBid = 0

    for name in auctionDict:
        bid = auctionDict[name]
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
        flag = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

        if flag == "yes":
            os.system('cls')
            flag = True
            name = input("What is your name?: ")
            bid = int(input("What's your bid?: $"))
            auctionDict[name] = bid

        elif flag == "no":
            sortBids(auctionDict)
            exit()

        else:
            print("Please input either 'yes' or 'no'\n")
            main(auctionDict)

main(auctionDict)