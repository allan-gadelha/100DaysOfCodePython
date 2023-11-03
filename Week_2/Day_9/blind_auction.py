logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#Creating Dict
bids = {}

while True:
    #Print art
    print(logo)
    
    #Intro
    print("Welcome to the secret auction program.")
    
    #Getting future key name
    name = input("What is your name: ")

    #Getting future value bid
    bid = int(input("What's your  bid?:  $"))

    #Feeding dict
    bids[name] = bid

    #Continue the program or not
    another = input("Are there any other bidders? Type 'yes' or 'no': ")
    if another == "no":
        break

#Highest Bid
max_bid = 0
#Winner
winner = ""

#Getting the highest bid and the Winner from dict!
for bidder, bid in bids.items():
    if bid > max_bid:
        max_bid = bid
        winner = bidder

print(f"The winner is {winner} with a bid of ${max_bid}")