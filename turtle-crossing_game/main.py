from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
level = Scoreboard()

screen.onkeypress(fun=player.move, key="Up")
screen.listen()

count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if count % 6 == 0 :
        cars.add_car()
    cars.move()
    count += 1

    if player.ycor() > 290:
        player.refresh()
        level.increase_level()
        cars.increase_speed()

    for car in cars.cars_list:
        if car.distance(player) < 30:
            level.game_over()
            game_is_on = False

    screen.update()

screen.exitonclick()
