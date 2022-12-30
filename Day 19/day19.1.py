# Day 19
# Etch-A-Sketch app
# This will alowe the user to control the turtle

from turtle import *

turtle = Turtle()
screen = Screen()


def antiClockwiseTurn():
    new_direction = turtle.heading() - 10
    turtle.setheading(new_direction)


def ClockwiseTurn():
    new_direction = turtle.heading() + 10
    turtle.setheading(new_direction)


def forward():
    turtle.forward(10)


def backward():
    turtle.backward(10)


def clearAndSetdefaultValue():
    turtle.reset


screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="a", fun=antiClockwiseTurn)
screen.onkeypress(key="d", fun=ClockwiseTurn)
screen.onkeypress(key="c", fun=clearAndSetdefaultValue)

screen.exitonclick()
