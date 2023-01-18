# Day 19
# This is an updated version of Trurle Race app

from turtle import *
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "green", "blue", "skyblue", "pink", "purple", "brown"]
spaceBetweenTurtles = [-150, -100, -50, 0, 50, 100, 150]
turtles = []

for turtle_index in range(0, 7):
    turtleName = Turtle("turtle")
    turtleName.penup()
    turtleName.color(colors[turtle_index])
    turtleName.setposition(-230, spaceBetweenTurtles[turtle_index])
    turtles.append(turtleName)

user_bet = screen.textinput(
    title="Make a bet", prompt="Which turtle will win the race? Enter a color: ").lower()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            is_race_on = False
            if user_bet == winner:
                turtle.write(
                    arg=f"You've won. The winner is {winner} turtle.", font=('Arial', 15, 'italic'), align='right')
            else:
                turtle.write(
                    arg=f"You've lost. The winner is {winner} turtle.", font=('Arial', 15, 'italic'), align='right')
screen.exitonclick()
