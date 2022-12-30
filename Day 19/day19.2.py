# Day 19
# Turtle race game

from turtle import *
import random

screen = Screen()
screen.setup(width=500, height=400)

# Initionalize all the turtles
red = Turtle("turtle")
green = Turtle("turtle")
blue = Turtle("turtle")
skyblue = Turtle("turtle")
pink = Turtle("turtle")
purple = Turtle("turtle")
brown = Turtle("turtle")

# We will not draw anything so the pen should be up
red.penup()
green.penup()
blue.penup()
skyblue.penup()
pink.penup()
purple.penup()
brown.penup()

# Colorized the turtle
red.color("red")
green.color("green")
blue.color("blue")
skyblue.color("skyblue")
pink.color("pink")
purple.color("purple")
brown.color("brown")

# Set setPositions of turles
# X cordinate of all turtle will be -230
red.setposition(-230, -150)
green.setposition(-230, -100)
blue.setposition(-230, -50)
skyblue.setposition(-230, 0)
pink.setposition(-230, 50)
purple.setposition(-230, 100)
brown.setposition(-230, 150)

# Ask from the user to bet on one of the turtle that this will win
user_bet = screen.textinput(
    title="Make a bet", prompt="Which turtle will win the race? Enter a color: ").lower()

# When the user bet set then we will start the race
if user_bet:
    is_race_on = True

while is_race_on:
    red.forward(random.randint(0, 10))
    green.forward(random.randint(0, 10))
    blue.forward(random.randint(0, 10))
    skyblue.forward(random.randint(0, 10))
    pink.forward(random.randint(0, 10))
    purple.forward(random.randint(0, 10))
    brown.forward(random.randint(0, 10))

    # Chose winner
    winner = ""
    if red.xcor() >= 230:
        winner = "red"
        is_race_on = False

        # Check that if the user won
        if user_bet == winner:
            print(f"You've won. The winner is {winner} turtle.")
        else:
            print(f"You've lost. The winner is {winner} turtle.")

    if green.xcor() >= 230:
        winner = "green"
        is_race_on = False

        # Check that if the user won
        if user_bet == winner:
            print(f"You've won. The winner is {winner} turtle.")
        else:
            print(f"You've lost. The winner is {winner} turtle.")
    if blue.xcor() >= 230:
        winner = "blue"
        is_race_on = False

        # Check that if the user won
        if user_bet == winner:
            print(f"You've won. The winner is {winner} turtle.")
        else:
            print(f"You've lost. The winner is {winner} turtle.")
    if skyblue.xcor() >= 230:
        winner = "skyblue"
        is_race_on = False

        # Check that if the user won
        if user_bet == winner:
            print(f"You've won. The winner is {winner} turtle.")
        else:
            print(f"You've lost. The winner is {winner} turtle.")
    if pink.xcor() >= 230:
        winner = "pink"
        is_race_on = False

        # Check that if the user won
        if user_bet == winner:
            print(f"You've won. The winner is {winner} turtle.")
        else:
            print(f"You've lost. The winner is {winner} turtle.")
    if purple.xcor() >= 230:
        winner = "purple"
        is_race_on = False

        # Check that if the user won
        if user_bet == winner:
            print(f"You've won. The winner is {winner} turtle.")
        else:
            print(f"You've lost. The winner is {winner} turtle.")
    if brown.xcor() >= 230:
        winner = "brown"
        is_race_on = False

        # Check that if the user won
        if user_bet == winner:
            print(f"You've won. The winner is {winner} turtle.")
        else:
            print(f"You've lost. The winner is {winner} turtle.")


screen.exitonclick()
