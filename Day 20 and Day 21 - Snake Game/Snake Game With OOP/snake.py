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
        self.head = self.snakeBody[0]

    def createSnake(self):
        for i in POSITIONS:
            self.add_snake(i)

    def add_snake(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.speed("fastest")
        snake.color("white")
        snake.setposition(position)
        self.snakeBody.append(snake)

    def extend(self):
        self.add_snake(self.snakeBody[-1].position())

    def move(self):
        """This will move the snake unlimited"""
        for snake in range(len(self.snakeBody) - 1, 0, -1):
            new_x = self.snakeBody[snake - 1].xcor()
            new_y = self.snakeBody[snake - 1].ycor()
            self.snakeBody[snake].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
