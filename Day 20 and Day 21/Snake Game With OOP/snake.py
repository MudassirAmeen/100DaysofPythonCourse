from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        """This will make snake"""
        self.snakeBody = []
        self.createSnake()

    def createSnake(self):
        for i in POSITIONS:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.setposition(i)
            self.snakeBody.append(snake)

    def move(self):
        """This will move the snake unlimited"""
        for snake in range(len(self.snakeBody) - 1, 0, -1):
            new_x = self.snakeBody[snake - 1].xcor()
            new_y = self.snakeBody[snake - 1].ycor()
            self.snakeBody[snake].goto(new_x, new_y)

        self.snakeBody[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snakeBody[0].heading() != DOWN:
            self.snakeBody[0].setheading(UP)

    def down(self):
        if self.snakeBody[0].heading() != UP:
            self.snakeBody[0].setheading(DOWN)

    def left(self):
        if self.snakeBody[0].heading() != RIGHT:
            self.snakeBody[0].setheading(LEFT)

    def right(self):
        if self.snakeBody[0].heading() != LEFT:
            self.snakeBody[0].setheading(RIGHT)
