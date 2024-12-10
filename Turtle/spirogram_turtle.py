import turtle
from turtle import Turtle , Screen
from random import choice, randint

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

def random_colour():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r,g,b)
    return color

tim.speed("fastest")
def draw_spirograpgh( radius , size_of_gap):
    for time in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_gap )

draw_spirograpgh(100 , 5)

my_screen = Screen()
my_screen.exitonclick()