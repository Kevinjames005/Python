from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier" , 40 , "bold")
class Scoreboard(Turtle):
    def __init__(self , x_cord , y_cord):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(x_cord , y_cord)
        self.score = 0
        self.score_update()

    def score_update(self):
        self.write(self.score, move=False , align=ALIGNMENT , font=FONT )

    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_update()

    def left_won(self):
        self.write("Left side won", move=False, align=ALIGNMENT, font=("Courier" , 16 , "normal"))

    def right_won(self):
        self.home()
        self.write("Right side won", move=False, align=ALIGNMENT, font=("Courier", 16, "normal"))
