import random


# get you a random card from deck - cards list
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)

    return random_card


# function to get the sum of the cards in hand
def sum_cards(cards):
    sum_cards = 0
    for card_value in cards:
        sum_cards += card_value

    if sum_cards > 21 and 11 in cards:
        # use ace as 1 instead as 11
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Player
player_cards = [deal_card(), deal_card()]
# Second player - dealer
dealer_cards = [deal_card(), deal_card()]


# Does someone have a blackJack?
def check_blackjack(players_card):
    has_blackjack = False
    if 11 in players_card and 10 in players_card:
        has_blackjack = True
    return has_blackjack


def play_blackjack():
    while True:
        print(f"Player's cards {player_cards} - {sum_cards(player_cards)} points")
        print(f"Dealer's face-up cards {dealer_cards[0]}")
        if check_blackjack(player_cards):
            print("Blackjack! - Player wins!")
        elif check_blackjack(dealer_cards):
            print("Blackjack! - Dealer wins!")
            break

        if sum_cards(player_cards) > 21:
            print("Dealer wins! - Player lost")
            break

        ask = input("Do you want an other card? 'y' / 'n' \n")
        if ask == 'y':
            player_cards.append(deal_card())
        else:
            while sum_cards(dealer_cards) < 17:
                dealer_cards.append(deal_card())
            print(f"Player's cards: {player_cards} - {sum_cards(player_cards)} points")
            print(f"Dealer's cards: {dealer_cards} - {sum_cards(dealer_cards)} points")

            if sum_cards(dealer_cards) > 21:
                print("Player wins! - Dealer lost")
            elif sum_cards(player_cards) > sum_cards(dealer_cards):
                print("Player wins!")
            elif sum_cards(player_cards) < sum_cards(dealer_cards):
                print("Dealer wins!")
            elif sum_cards(player_cards) == sum_cards(dealer_cards):
                print("Drawn!")

            break


play_blackjack()
