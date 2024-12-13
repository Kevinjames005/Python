from turtle import Turtle , Screen
import time

screen = Screen()
screen.setup(width = 600 , height = 600)
screen.title("My Snake Game")
screen.bgcolor("black")
blocks = []
y = 0
x = 0
screen.tracer(0)
for i in range(3):
    new_block= Turtle(shape = "square" )
    new_block.penup()
    new_block.color("white")
    new_block.setposition(x=x , y = y)
    x += -20
    blocks.append(new_block)

def move_right():
    blocks[0].setheading(0)
    blocks[0].forward(10)
def move_left():
    blocks[0].setheading(180)
    blocks[0].forward(10)
def move_up():
    blocks[0].setheading(90)
    blocks[0].forward(10)
def move_down():
    blocks[0].setheading(270)
    blocks[0].forward(10)



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.onkeypress(fun=move_left, key="Left")
    screen.onkeypress(fun=move_right, key="Right")
    screen.onkeypress(fun=move_up, key="Up")
    screen.onkeypress(fun=move_down, key="Down")
    screen.listen()

    for seg_num in range(len(blocks)-1, 0 , -1):
        new_x = blocks[seg_num - 1].xcor()
        new_y = blocks[seg_num - 1].ycor()
        blocks[seg_num].goto(new_x,new_y)
    screen.update()















screen.exitonclick()