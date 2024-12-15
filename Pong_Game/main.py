from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.title("My Pong Game")
screen.bgcolor("black")
screen.setup(width = 800 , height = 600)

screen.tracer(0)
left_score = Scoreboard( -40 , 230)
right_score = Scoreboard(40 , 230)

ball = Ball()

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350 , 0)

screen.onkeypress(fun = r_paddle.move_up , key = "Up")
screen.onkeypress(fun = r_paddle.move_down , key = "Down")
screen.onkeypress(fun = l_paddle.move_up , key = "w")
screen.onkeypress(fun = l_paddle.move_down , key = "s")
screen.listen()

game_is_on = True
slow_time = 0.015
while game_is_on:
    time.sleep(slow_time)
    ball.ball_move()

    #Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

    #Detect collision with paddle
    if (ball.xcor() > 340 and ball.distance(r_paddle) < 50) or(ball.xcor() < -340 and ball.distance(l_paddle) < 50):
        ball.paddle_bounce()
        slow_time -= 0.0001

    #Detect out of bounds and increase score
    if ball.xcor() > 390 or ball.xcor() < -390:
        if ball.xcor() > 390:
            ball.ball_reset()
            left_score.score_increase()
        else :
            ball.ball_reset()
            right_score.score_increase()
        slow_time = 0.015

    screen.update()

screen.exitonclick()
