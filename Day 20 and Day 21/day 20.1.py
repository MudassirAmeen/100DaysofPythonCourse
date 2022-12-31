# Day 20
# In this day we will build a Snake Game

from turtle import *
import time

# Make a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# We have to stop the animation
screen.tracer()

# 1. Make a Snake => The snake will be three turtles one after one
snakeBody = []
positions = [(0, 0), (-20, 0), (-40, 0)]
for i in positions:
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.setposition(i)
    snakeBody.append(snake)


# 3. Control the snake => we will use Up, Down, Left, Right key to controll the snake
def up():
    if snakeBody[0].heading() != 270:
        snakeBody[0].setheading(90)
def down():
    if snakeBody[0].heading() != 90:
        snakeBody[0].setheading(270)
def left():
    if snakeBody[0].heading() != 0:
        snakeBody[0].setheading(180)
def right():
    if snakeBody[0].heading() != 180:
        snakeBody[0].setheading(0)
screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(right,"Right")
screen.onkey(left,"Left")


# 2. Move the snake => we need while loop to continuously move the snake
Game_is_on = True
while Game_is_on:
    # As we have stop the animation so we need update method to start the animation
    screen.update()
    time.sleep(0.1)

    # Problem 1 => Goto to readme file to understan what is this problem solution
    # for snake in snakeBody:
    #     snake.forward(10)

    # Solution Problem 1
    for snake in range(len(snakeBody) - 1, 0, -1):
        new_x = snakeBody[snake - 1].xcor()
        new_y = snakeBody[snake - 1].ycor()
        snakeBody[snake].goto(new_x, new_y)

    snakeBody[0].forward(20)

screen.exitonclick()
