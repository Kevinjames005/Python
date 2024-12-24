from turtle import Turtle


class State_name(Turtle):
    def __init__(self,state_name , x_coordinate , y_coordinate):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=x_coordinate, y=y_coordinate)
        self.write(state_name,move = False,align="center" , font=("Arial",10,"normal"))
