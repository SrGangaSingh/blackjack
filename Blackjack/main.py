import random

print(""""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/ 
""")


def main():
    deck = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    your_cards = [random.choice(deck), random.choice(deck)]
    com_cards = [random.choice(deck), random.choice(deck)]

    show_cards(your_cards, com_cards)

    your_sum = sum(your_cards)
    com_sum = sum(com_cards)

    while True:
        if blackjack(your_sum, com_sum):
            break
        your_move = input(
            "Type 'y' to get another card, type 'n' to pass: ").lower()
        com_move = random.choice([True, False])

        if your_move == "n":
            if not com_move:
                show_final_cards(your_cards, com_cards)
                break
            else:
                com_cards.append(random.choice(deck))
                com_cards = aceBonus(com_cards)
                com_sum = sum(com_cards)
                if com_sum >= 21:
                    show_final_cards(your_cards, com_cards)
                    break
                print("Your final hand:", your_cards)
                print("Computer's first card:", com_cards[0])

        elif your_move == "y":
            your_cards.append(random.choice(deck))
            your_cards = aceBonus(your_cards)
            your_sum = sum(your_cards)

            if not com_move:
                if your_sum >= 21:
                    show_final_cards(your_cards, com_cards)
                    break

                show_cards(your_cards, com_cards)
            else:
                com_cards.append(random.choice(deck))
                com_cards = aceBonus(com_cards)
                com_sum = sum(com_cards)

                if your_sum >= 21 or com_sum >= 21:
                    show_final_cards(your_cards, com_cards)
                    break
                show_cards(your_cards, com_cards)


def show_cards(your_cards, com_cards):
    print("your_cards:", your_cards, "| Sum:", sum(your_cards))
    print("Computer's first card:", com_cards[0])


def show_final_cards(your_cards, com_cards):
    print("Your final hand:", your_cards, "| Sum:", sum(your_cards))
    print("Computer's final hand:", com_cards, "| Sum:", sum(com_cards))
    check_winner(sum(your_cards), sum(com_cards))


def check_winner(your_sum, com_sum):
    if (your_sum > com_sum and your_sum <= 21) or (your_sum <= 21 and com_sum > 21):
        print("You Win")
    elif your_sum == com_sum and (your_sum <= 21 and com_sum <= 21):
        print("Draw")
    else:
        print("You lose")


def blackjack(your_sum, com_sum):
    if your_sum == 21 and com_sum == 21:
        print("Draw, both got a blackjack")
        return True
    if your_sum == 21:
        print("BlackJack, You Win")
        return True
    if com_sum == 21:
        print("You lose, computer's got a BlackJack")
        return True
    return False


def aceBonus(cards):
    if 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
        return cards
    return cards


if __name__ == "__main__":
    while input("You want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
        main()
