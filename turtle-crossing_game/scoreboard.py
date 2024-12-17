from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-210 , 250)
        self.initial_level()


    def initial_level(self):
        self.write(f"Level  {self.level}" , move = False , align="center" , font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.initial_level()

    def game_over(self):
        self.home()
        self.write("Game Over", move=False, align="center", font=("Courier", 13 , "normal"))