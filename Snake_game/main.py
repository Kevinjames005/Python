from turtle import  Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600 , height = 600)
screen.title("My Snake Game")
screen.bgcolor("black")

screen.tracer(0)
snake = Snake()
screen.onkeypress(fun=snake.move_left, key="Left")
screen.onkeypress(fun=snake.move_right, key="Right")
screen.onkeypress(fun=snake.move_up, key="Up")
screen.onkeypress(fun=snake.move_down, key="Down")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()















screen.exitonclick()




