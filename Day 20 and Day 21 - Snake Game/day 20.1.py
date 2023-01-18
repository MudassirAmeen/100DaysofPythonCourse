# Day 20
# In this day we will build a Snake Game

from turtle import *
import time, random

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
    snake.speed("fastest")
    snakeBody.append(snake)

def extend():
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.setposition(i)
    snake.speed("fastest")
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


# 4. Make a food => we can make a food from Turtle class
food = ""

def Food():
    global food
    food = Turtle("circle")
    food.shapesize(stretch_len=0.5, stretch_wid=0.5)
    food.color("blue")
    food.penup()
    food.speed(0)

def changePositionOfFood():
    food.goto(random.randint(-280, 280), random.randint(-280, 280))

Food()
changePositionOfFood()

# 6. SHow the score of player
score = 0
scoreBoard = Turtle()
def scoreboard():
    global score, scoreBoard
    scoreBoard.penup()
    scoreBoard.hideturtle()
    scoreBoard.color("white")
    scoreBoard.clear()
    scoreBoard.goto(0, 260)
    scoreBoard.write(arg=f"Score: {score}", align="center", font=("Arial", 19, "normal"))


def updateScore():
    global score, scoreBoard
    scoreBoard.clear()
    score += 1
    scoreBoard.write(arg=f"Score: {score}", align="center", font=("Arial", 19, "normal"))

scoreboard()

# 8. Game over function
def game_over():
    global scoreBoard
    scoreBoard.goto(0,0)
    scoreBoard.write(arg="Game Over", align="center", font=("Arial", 19, "normal"))



# 2. Move the snake => we need while loop to continuously move the snake
Game_is_on = True
while Game_is_on:
    # As we have stop the animation so we need update method to start the animation
    screen.update()
    time.sleep(0.1)
    snakeBody[0].forward(20)

    # Problem 1 => Goto to readme file to understan what is this problem solution
    # for snake in snakeBody:
    #     snake.forward(10)

    # Solution Problem 1
    for snake in range(len(snakeBody) - 1, 0, -1):
        new_x = snakeBody[snake - 1].xcor()
        new_y = snakeBody[snake - 1].ycor()
        snakeBody[snake].goto(new_x, new_y)


    # 5. When a snake colied with the food then the food should go to another point
    if snakeBody[snake].distance(food) < 15:
        changePositionOfFood()
        extend()
        # 7. Update the score
        updateScore()
    
    # 8. Game Over
    if snakeBody[0].xcor() < -280 or snakeBody[0].xcor() > 280 or snakeBody[0].ycor() < -280 or snakeBody[0].ycor() > 280:
        Game_is_on = False
        game_over()

    # # 9. Detect collision with snake itself
    # for segment in snakeBody:
    #     if segment == snakeBody[snake]:
    #         pass
    #     elif snakeBody[snake].distance(segment) < 10:
    #         Game_is_on = False
    #         game_over()

screen.exitonclick()
