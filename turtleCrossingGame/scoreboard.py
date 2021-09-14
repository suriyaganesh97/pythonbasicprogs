from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-200, 240)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Level : {self.score}", align="center", font=(FONT))

    def score_up(self):
        self.score += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)