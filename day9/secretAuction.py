import os

auction_dictionary = {}
finished = False

while not finished:
    name = input("What is your name?\n")
    bid = float(input("What is your bid?\n"))  # Convert bid to a floating-point number
    auction_dictionary[name] = bid  # Store the bid using the person's name as the key

    choice = input("Are there other persons? 'yes' / 'no' ?\n")
    if choice == "no":
        finished = True
        max_bidder = max(auction_dictionary, key=auction_dictionary.get)  # Get the key (name) with the maximum bid
        max_bid = auction_dictionary[max_bidder]  # Get the maximum bid
        print(f"The winner is {max_bidder} with a bid of {max_bid}")
    elif choice == "yes":
        os.system('cls')


