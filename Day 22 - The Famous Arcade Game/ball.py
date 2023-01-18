from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1

    def moveBall(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)
   
    def bouns_y(self):
        self.y_cor *= -1

    def bouns_x(self):
        self.x_cor *= -1
        self.move_speed *= 0.5

    def reset_position(self):
        self.goto(0,0)
        self.bouns_x()