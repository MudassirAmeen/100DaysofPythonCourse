# Day 11

import random
import replit

# In this day we will make our game named Black Jack Game. 

# What are the rules for this game
# 1. If your score is greater then computer score then you will win
# 2. If your score is less then computer score then you will lose
# 3. If your score is greater the 21 then you will also lose 

# First of all we have to make a cards list from which we will get cards.

# In the card list first 10 = A, and after 9, 10, the first 10 = J, second = Q, third = K
cards = [10 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]


# These are some veriables that we will used 
Your_card = []
Computer_card = []
Your_score = 0
Computer_score = 0

# Function for the whole game
def deal_card():
    # We have make this veriable because this will be used to get two values from the cards list
    times = 1
    while times <= 2:
        Your_card.append(random.choice(cards))
        times += 1
    Your_score = sum(Your_card)
    if Your_score == 21:
        Your_score = 0
        print("hi")
    Computer_card.append(random.choice(cards))
    Computer_card.append("?")
    print(f"Your Card : {Your_card} \t Your score : {Your_score}")
    print(f"Computer Card : {Computer_card}")
    
    Question = input("Type'y' to get another card, type 'n' to pass : ")

    if Question == "y":
        Your_card.append(random.choice(cards))
        Computer_card[1] = random.choice(cards)
        Your_score = sum(Your_card)
        Computer_score = sum(Computer_card)
        if Your_score > 21:
            print(f"Your Card : {Your_card} \t Your score : {Your_score}")
            print("You lose becaause your score is greater then 21. 😢")
            Your_card.clear()
            Computer_card.clear()
        else:
            choseWinner(score1 = Your_score, score2 = Computer_score)
    else:
        Computer_card[1] = random.choice(cards)
        Computer_score = sum(Computer_card)
        choseWinner(score1 = Your_score, score2 = Computer_score)
def choseWinner(score1, score2):
    print(f"Your Card : {Your_card} \t Your score : {score1}")
    print(f"Computer Card : {Computer_card} \t Computer Score : {score2}")
    if score1 > score2:
        print("You win.🏆")
    else:
        print("You lose.😢")
    Your_card.clear()
    Computer_card.clear()
    print(Your_card)
    print(Computer_card)
condition = True
while condition:
    print('''
 _______                     ___                                      ____    ____  ______    
|_   __ \                  .' ..]                                    |_   \  /   _||_   _ `.  
  | |__) |_ .--.   .--.   _| |_  .---.  .--.   .--.   .--.   _ .--.    |   \/   |    | | `. \ 
  |  ___/[ `/'`\]/ .'`\ \'-| |-'/ /__\\( (`\] ( (`\]/ .'`\ \[ `/'`\]   | |\  /| |    | |  | | 
 _| |_    | |    | \__. |  | |  | \__., `'.'.  `'.'.| \__. | | |      _| |_\/_| |_  _| |_.' / 
|_____|  [___]    '.__.'  [___]  '.__.'[\__) )[\__) )'.__.' [___]    |_____||_____||______.'  
                                                                                              
''')
    deal_card()
    Question = input("Do you want to play the Blackjack Game? Type 'y' or 'n' ")
    if Question != "y":
        condition = False
        replit.clear()
    else:
        replit.clear()