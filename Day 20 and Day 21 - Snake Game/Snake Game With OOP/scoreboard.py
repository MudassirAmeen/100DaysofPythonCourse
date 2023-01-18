from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 19, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.clear()
        self.goto(0, 260)
        self.scoreBoard()
    
    def scoreBoard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game over", align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.score += 1
        self.clear()
        self.scoreBoard()
