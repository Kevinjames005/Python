from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 13, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0,275)
        self.update_score()


    def update_score(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER" , move = False , align=ALIGNMENT, font=FONT)






