# import colorgram
#
# colors = colorgram.extract('image.jpg',30)
# color_rgb =[]
#
# for color in colors:
#     color_rgb.append(tuple(color.rgb))
#
# print(color_rgb)
import turtle
from turtle import Turtle, Screen
from random import choice
turtle.colormode(255)
colour_list = [ (14, 20, 76), (220, 151, 88), (237, 228, 99), (34, 94, 155), (133, 25, 54), (206, 82, 118), (187, 77, 30), (50, 29, 19), (119, 177, 216), (20, 46, 138), (16, 47, 28), (228, 74, 49), (4, 100, 36), (204, 132, 171), (161, 57, 87), (92, 201, 161), (71, 23, 36), (25, 134, 51), (141, 213, 186), (166, 16, 10), (95, 112, 197), (251, 225, 1), (85, 82, 20), (19, 174, 138), (15, 172, 208), (236, 167, 154)]

tim = Turtle()

tim.speed("fastest")
tim.hideturtle()
tim.shape("turtle")
tim.penup()
x = -225
y = -200
while y < 300:
    tim.teleport(x , y)
    for i in range(10):
        tim.dot(20 , choice(colour_list))
        tim.forward(50)
    y += 50














my_screen = Screen()
my_screen.exitonclick()