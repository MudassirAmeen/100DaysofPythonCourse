# Day 20
# In this day we will build a Snake Game

from turtle import *
import time
from snake import Snake

# Make a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# We have to stop the animation
screen.tracer()

# 1. Make a snake
snake = Snake()

# 3. Controll the snake => we will use Up, Down, Left, Right key to controll the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

# 2. Move the snake => we need while loop to continuously move the snake
Game_is_on = True
while Game_is_on:
    # As we have stop the animation so we need update method to start the animation
    screen.update()
    time.sleep(0.2)

    snake.move()

screen.exitonclick()
