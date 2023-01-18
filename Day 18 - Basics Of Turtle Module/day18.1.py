from turtle import Turtle, Screen
square = Turtle()
def move_and_turn_right():
    square.forward(100)
    square.right(90)
for _ in range(0,4):
    move_and_turn_right()

screen = Screen()
screen.exitonclick()
