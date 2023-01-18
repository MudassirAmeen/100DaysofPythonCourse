# This is day 4

# We will need modules
import random

# In this day we will make a rock, paper, scissors game using Python

# First of all we will make ASCII ARTS for the rock, paper, scissor 
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Rules for this game is very simple. 
# 1. Rock will win against scissor
# 2. Scissor will win against paper
# 3. Paper will win against rock

# Follow that rules and we will make a program that will play the Rock, Scissor, Paper game with us

game = [rock,scissor,paper]

# Now we first computer will select one thing

computer_turn = random.choice(game)

# After that we will ask the user to select one thing

user_turn = input("What is your choice? Rock, Paper, Scissor : ").lower()

# Fill out first rule

if computer_turn == rock:

    print("rock")
    print(rock)

    if user_turn == "rock":

        print("rock")
        print(rock)

        print("This match is tie. Try again.")

    elif user_turn == "paper":

        print("paper")
        print(paper)

        print("You win.😁")

    elif user_turn == "scissor":

        print("scissor")
        print(scissor)

        print("You lose.🤥")

    else:

        print("Please select right option.")

elif computer_turn == paper:

    print("paper")
    print(paper)

    if user_turn == "paper":

        print("paper")
        print(paper)

        print("This match is tie. Try again.")

    elif user_turn == "scissor":

        print("scissor")
        print(scissor)

        print("You win.😁")

    elif user_turn == "rock":

        print("rock")
        print(rock)

        print("You lose.🤥")

    else:

        print("Please select right option.")

elif computer_turn == scissor:

    print("scissor")
    print(scissor)

    if user_turn == "scissor":

        print("scissor")
        print(scissor)

        print("This match is tie. Try again.")

    elif user_turn == "rock":

        print("rock")
        print(rock)

        print("You win.😁")

    elif user_turn == "paper":

        print("paper")
        print(paper)

        print("You lose.🤥")

    else:

        print("You typed wrong. So, you are lose.🤥")
