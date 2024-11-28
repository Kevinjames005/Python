Auction = {}
print(
    '''
                         ___________
                         \\         /
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
)
print("Welcome to the Secret Auction Program.")

bid_continue = True
while bid_continue :
    key = input("What is your name? : ")
    Auction[key] = int(input("What is your bid : $"))
    like_to_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    print("\n" * 100)
    if like_to_continue == "no":
        bid_continue = False

max_bid = 0
name = ""
for bid in Auction:
    if Auction[bid] > max_bid :
        name = bid
        max_bid = Auction[bid]

print(f"The winner is {name} with a bid of ${max_bid}")


