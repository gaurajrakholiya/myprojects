import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculated_score(cards):
    return sum(cards)

def compare(user_score, computer_score):
    
    if user_score > 21 and computer_score > 21:
        print("you went over ! you lose")

    if user_score == computer_score :
        print("Draw !")
    elif user_score > 21:
        print("opponent win the game")
    elif computer_score > 21:
        print("you win")
    elif computer_score == 0 :
        print("opponent get the blackjack")
    elif user_score == 0:
        print("you get the blackjack")
    elif user_score > computer_score:
        print("you win")
    else:
        print("you lose")

    
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculated_score(user_cards)
        computer_score = calculated_score(computer_cards)
        if input("do you want to play type 'y' for yes or 'n' for no?") == "y":
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {computer_cards[0]}")
        else:
            is_game_over = True
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("you want to add something 'y' for yes or 'n' for no") == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    
    play_game()