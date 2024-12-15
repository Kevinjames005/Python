from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cord , y_cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed("fastest")
        self.penup()
        self.goto(x_cord, y_cord)

    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_down(self):
        self.setheading(270)
        self.forward(10)