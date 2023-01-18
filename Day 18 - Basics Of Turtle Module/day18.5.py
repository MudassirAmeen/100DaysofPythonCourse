import turtle as t
import random as ra

circle = t.Turtle()
circle.speed(0)
degree = 1
t.colormode(255)
def random_color():
    r = ra.randint(0, 255)
    g = ra.randint(0, 255)
    b = ra.randint(0, 255)
    random_color = (r, g, b)
    return random_color
def draw_circle(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        circle.circle(100)
        circle.setheading(circle.heading() + size_of_gap)
        circle.color(random_color())

draw_circle(5)
screen = t.Screen()
screen.exitonclick()


