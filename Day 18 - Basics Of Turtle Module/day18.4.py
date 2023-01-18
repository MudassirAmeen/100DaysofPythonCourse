from turtle import *
from random import *
colors = ["red","orange","green","blue","indigo","violet","black","gray"]
line = Turtle()
line.speed(0)
for _ in range(200):
    degree = choice([0, 90, 180, 270])
    line.pensize(10)
    line.forward(30)
    line.setheading(degree)
    line.color(choice(colors))
    # line.forward(20)

screen = Screen()
screen.exitonclick()