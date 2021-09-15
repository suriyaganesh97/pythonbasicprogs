from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.initial_score = 0
        #self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score = {self.initial_score}", align=ALIGNMENT, font=FONT)


    def score_update(self):
        self.initial_score += 1
        self.clear()
        self.write(f"Score = {self.initial_score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
