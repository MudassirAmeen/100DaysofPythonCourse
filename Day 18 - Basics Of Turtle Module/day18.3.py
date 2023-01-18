from turtle import *
from random import *

line = Turtle()
deg = 120
corners = 3
colors = ["red", "orange", "green", "blue", "purple"]
for i in range(10):
    for _ in range(corners):
        line.forward(100)
        line.left(deg)
    line.color(choice(colors))
    corners += 1
    deg = 360 / corners
screen = Screen()
screen.exitonclick()