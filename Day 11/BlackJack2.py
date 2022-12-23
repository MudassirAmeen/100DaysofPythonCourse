# Day 11
import random,replit

# In this day we will make a blackjack game.

# This function will return random one card form the deck
def deal_card():
    """This function will return a random card from the deck"""
    cards = [10 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]
    return random.choice(cards)

# This will return the sum of the cards
def calculate(cards):
    """Take a list and return sum of that list"""
    # if we have score of 21 at the start then we have to return 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 📍"
    elif computer_score == 0:
        return "You lose, Computer has a Blackjack"
    elif user_score == 0:
        return "You win, Because you have a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "You win. Because computer went over"
    elif computer_score > user_score:
        return "You lose. Because computer has more score then you"
    else:
        return "You win. "
def play_game():
    print('''
 _______                     ___                                      ____    ____  ______    
|_   __ \                  .' ..]                                    |_   \  /   _||_   _ `.  
  | |__) |_ .--.   .--.   _| |_  .---.  .--.   .--.   .--.   _ .--.    |   \/   |    | | `. \ 
  |  ___/[ `/'`\]/ .'`\ \'-| |-'/ /__\\( (`\] ( (`\]/ .'`\ \[ `/'`\]   | |\  /| |    | |  | | 
 _| |_    | |    | \__. |  | |  | \__., `'.'.  `'.'.| \__. | | |      _| |_\/_| |_  _| |_.' / 
|_____|  [___]    '.__.'  [___]  '.__.'[\__) )[\__) )'.__.' [___]    |_____||_____||______.'  
                                                                                              
''')
    # This function will add the a random item from the deck in Your_card list and Computer_card list
    Your_card = []
    Computer_card = []
    is_game_over = False

    for _ in range(2):
        Your_card.append(deal_card())
        Computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate(Your_card)
        computer_score = calculate(Computer_card)
        print(f"Your card : {Your_card} , Your_score : {user_score}")
        print(f"Computer first card : {Computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass ")
            if user_should_deal == "y":
                Your_card.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        Computer_card.append(deal_card())
        computer_score = calculate(Computer_card)

    print(f"Your Card : {Your_card} \t Your score : {user_score}")
    print(f"Computer Card : {Computer_card} \t Computer Score : {computer_score}")
    print(compare(user_score = user_score, computer_score = computer_score))

while input("Do you want to play the Blackjack Game? Type 'y' or 'n' ").lower() == "y":
    replit.clear()
    play_game()