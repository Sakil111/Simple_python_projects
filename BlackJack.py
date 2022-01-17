import random
def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    """ Take a list of card and return the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You won"
    elif computer_score == 0:
        return "You lose, opponent won"
    elif user_score > 21:
        return "You lose, opponent won"
    elif computer_score > 21:
        return "You won, opponent over"
    elif user_score > computer_score:
        return "You won"
    else:
        return "You lose"

user_cards=[]
computer_cards=[]
is_game_over=False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"user card: {user_cards},current score={user_score}")
    print(f"computer's first card:{computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("types 'y' to get another card, type 'y' to pass: ")
        if user_should_deal=="y":
            user_cards.append(deal_card())
        else:
            is_game_over=True

while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

print(f"You final hand: {user_cards}")
print(f"Computer final hand:{computer_cards}")
print(compare_score(user_score,computer_score))