#########################################################
###############      SECRET AUCTION        ##############
#########################################################

bidderDict = {}
flag = True

# def sortBids():

def main(bidderDict, name, bid):
    while flag == True:
        i += i
        flag = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if flag == "yes":
            flag = True
        elif flag == "no":
            exit # Replace this with sorting algorithm to display winner of bid
        else:
            flag = input("Please input either 'yes' or 'no'\n")
            main()

        name = input("What is your name?: ")
        bid = int(input("What's your bid?: "))

        bidderDict[name][bid]

name = str(input("What is your name?: "))
bid = int(input("What's your bid?: $"))
bidderDict[name][bid]

main(bidderDict, name, bid)