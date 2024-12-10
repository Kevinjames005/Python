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



def random_walk(number_of_times):
    for times in range(number_of_times):
        tim.color(random_colour())
        random_rotation = [0,90,180,270]
        tim.setheading(choice(random_rotation))
        tim.forward(30)
tim.pensize(5)
tim.speed("fastest")
random_walk(200)

my_screen = Screen()
my_screen.exitonclick()