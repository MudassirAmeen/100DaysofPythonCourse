# Day 12

# In this day we will make a game that will ask you to guess a number which I have.

# There will be two deficulties Easy and Hard. 
# In the easy you will have 10 lives
# In the hard you will have 5 lives

import random, replit

# Function to tell us that user guess word is too high or to low or equal
def check_number(chosenNumber, user_guess):
    """Check the user guess Number"""
    if user_guess == chosenNumber:
        return 0
    elif user_guess > chosenNumber:
        return 1
    else:
        return 2

# Function to chose a deficulty level
def choseDeficulty():
    """This will check the deficulty level that user chose"""
    chooseDeficulty = input("Choose a deficulty. Type 'easy' or 'hard' : ")
    if chooseDeficulty == "hard":
        return 1
    else:
        return 0
# Chose Number function
def play_game():
    print('''
 _______                     ___                                      ____    ____  ______    
|_   __ \                  .' ..]                                    |_   \  /   _||_   _ `.  
  | |__) |_ .--.   .--.   _| |_  .---.  .--.   .--.   .--.   _ .--.    |   \/   |    | | `. \ 
  |  ___/[ `/'`\]/ .'`\ \'-| |-'/ /__\\( (`\] ( (`\]/ .'`\ \[ `/'`\]   | |\  /| |    | |  | | 
 _| |_    | |    | \__. |  | |  | \__., `'.'.  `'.'.| \__. | | |      _| |_\/_| |_  _| |_.' / 
|_____|  [___]    '.__.'  [___]  '.__.'[\__) )[\__) )'.__.' [___]    |_____||_____||______.'  
                                                                                              
''')
    print("Welcome to Professor MD Guess Word Game.")
    choseNumber = random.randint(1, 100)
    end_game = False
    chooseDeficulty = choseDeficulty()
    if chooseDeficulty == 1:
        lives = 5
    if chooseDeficulty == 0:
        lives = 10
    live = lives
    while live != 0:
        while end_game != True:
            if live < 1:
                end_game = True
                print(f"Your lives are {live}.")
                print(f"The number was {choseNumber}")
                return "You lose"
            print(f"Your remaining lives are {live}.")
            user_guess = int(input("Chose a number : "))
            result = check_number(chosenNumber = choseNumber, user_guess = user_guess)
            if result == 0:
                end_game = True
                return "You win.😉🥇"
            elif result == 1:
                live -= 1
                print("Too high")
            else:
                live -= 1
                print("Too low")

print(play_game())
if input("Do you want to play again. Type 'y' or 'n' : ") == 'y':
    replit.clear()
    print(play_game())