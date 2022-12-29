import turtle as t
import random as ran

t.colormode(255)
colors = [
    (255, 0, 0),  # red
    (0, 255, 0),  # green
    (0, 0, 255),  # blue
    (255, 255, 0),  # yellow
    (128, 0, 128),  # purple
    (0, 128, 128),  # teal
    (255, 192, 203),  # pink
    (255, 165, 0),  # orange
    (128, 0, 0),  # maroon
    (128, 128, 0),  # olive
    (255, 0, 255),  # magenta
    (230, 230, 250),  # lavender
    (210, 180, 140),  # tan
    (250, 128, 114),  # salmon
    (255, 127, 80),  # coral
    (255, 99, 71),  # tomato
    (160, 82, 45),  # sienna
    (255, 218, 185),  # peach
    (135, 206, 235),  # sky blue
    (144, 238, 144),  # light green
    (173, 216, 230),  # light blue
    (248, 248, 255),  # light purple
    (255, 182, 193),  # light pink
    (255, 160, 122),  # light orange
    (255, 255, 224),  # light yellow
    (210, 180, 140),  # light brown
    (255, 99, 71),  # light red
    (211, 211, 211),  # light grey
    (0, 100, 0),  # dark green
    (0, 0, 139)  # dark blue
]

dot = t.Turtle()

dot.up()
dot.hideturtle()
dot.speed(0)
dot.setheading(225)
dot.forward(300)
dot.setheading(0)

for height in range(10):

    for width in range(10):
        dot.dot(20, ran.choice(colors))
        dot.forward(50)

    dot.setheading(90)
    dot.forward(50)
    dot.setheading(360)
    dot.backward(500)

screen = t.Screen()
screen.exitonclick()