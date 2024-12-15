from turtle import  Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600 , height = 600)
screen.title("My Snake Game")
screen.bgcolor("black")



screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

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

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_increase()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score.game_over()
        game_is_on = False

    #Detect collision with tail
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10 :
            game_is_on = False
            score.game_over()


screen.exitonclick()
