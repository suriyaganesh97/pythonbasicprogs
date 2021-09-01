import random
card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []
is_game_over = False


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "computer wins with a blackjack"
    elif user_score == 0:
        return "user wins with a blackjack"
    elif user_score > 21:
        return "you went over. you lose"
    elif computer_score > 21:
        return "computer went over.computer losses"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"


def deal_card():
    card = random.choice(card_values)
    return card


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"the user cards is {user_cards} score is {user_score}")
    print(f"the computer first card is {computer_cards[0]}")
    if computer_score == 0 or user_score == 0 or user_score > 21:
        is_game_over = True
    user_should_deal = input("type 'y' to get another card and 'n' to not get a card")
    if user_should_deal == 'y':
        user_cards.append(deal_card())
    else:
        is_game_over = True
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"your cards are {user_cards} and score is {user_score}")
print(f"computer cards are {computer_cards} and score is {computer_score}")
print(compare(user_score, computer_score))
