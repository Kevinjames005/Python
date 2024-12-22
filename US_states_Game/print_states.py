from turtle import Turtle


class print_state(Turtle):
    def __init__(self,state_name , x_cordinate , y_cordinate):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.write(state_name,move = False,align="center" , font=("Arial",8,"normal"))
        self.goto(x = x_cordinate , y = y_cordinate)