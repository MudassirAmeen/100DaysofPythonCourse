from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# 1. make a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer()

# 2. Create Paddles
rightPaddle = Paddle(380, 0)
leftPaddle = Paddle(-380, 0)
# 4. Create a ball
ball = Ball()
# 9. Create a scoreboard
score = Scoreboard()

# 3. Listen for key press
screen.listen()
screen.onkey(rightPaddle.up, "Up")
screen.onkey(rightPaddle.down, "Down")
screen.onkey(leftPaddle.up, "w")
screen.onkey(leftPaddle.down, "s")

Game_is_on = True
while Game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moveBall()

    # 5. Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouns_y()

    # 6. Detect collosion with padddles
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 360 or ball.distance(leftPaddle) < 50 and ball.xcor() < -360:
        ball.bouns_x()

    # 7. Detect miss with right paddle
    if ball.xcor() > 400:
        ball.reset_position()
        score.l_point()

    # 8. Detect miss with left paddle
    if ball.xcor() < -400:
        ball.reset_position()
        score.r_point()





screen.exitonclick()

