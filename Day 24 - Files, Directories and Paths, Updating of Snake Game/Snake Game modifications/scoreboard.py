from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 19, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.clear()
        self.goto(0, 260)
        self.scoreBoard()
    
    def scoreBoard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            data = open("Day 24\Snake Game modifications\data.txt", "w")
            data.write(str(self.highscore))
        self.score = 0
        self.scoreBoard()

    def updateScore(self):
        self.score += 1
        self.scoreBoard()
