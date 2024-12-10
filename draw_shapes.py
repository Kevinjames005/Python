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

def shapes_of_nsides(no_of_side):
    """This function draws the shape based on number of sides"""
    angle = 360 / no_of_side
    for side in range(no_of_side):
        tim.forward(100)
        tim.right(angle)

for shape in range(3,11):
    tim.color(random_colour())
    shapes_of_nsides(shape)

my_screen = Screen()
my_screen.exitonclick()