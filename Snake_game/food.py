from turtle import Turtle

import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.refresh()

    def refresh(self):
        rand_x_coordinate = random.randint(-280, 280)
        rand_y_coordinate = random.randint(-280, 280)
        self.goto(x=rand_x_coordinate, y=rand_y_coordinate)


