from turtle import Turtle
with open("data.txt", mode="r") as file:
    score = int(file.read())


ALIGNMENT = "center"
FONT = ("Arial", 13, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = score
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0,275)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}   High Score = {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        self.update_score()

    def update_high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{(self.highscore)}")
        self.score = 0
        self.update_score()







