from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.move_paddle = 20
        self.goto(xcor, ycor)

    def up(self):
        self.new_y = self.ycor() + self.move_paddle
        self.goto(self.xcor(), self.new_y)

    def down(self):
        self.new_y = self.ycor() - self.move_paddle
        self.goto(self.xcor(), self.new_y)

