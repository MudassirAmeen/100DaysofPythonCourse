from turtle import *
dashed = Turtle()
for i in range(15):
    dashed.down()
    dashed.forward(10)
    dashed.up()
    dashed.forward(10)


screen = Screen()
screen.exitonclick()