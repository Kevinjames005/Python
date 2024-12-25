import turtle
import pandas
from print_states import State_name

screen = turtle.Screen()
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data.state
x_coordinates = data.x
y_coordinates = data.y
states_list = states.to_list()
x_coordinates_list = x_coordinates.to_list()
y_coordinates_list = y_coordinates.to_list()
title_prompt = "Guess the states"
count = 0
total = 50

game_on = True
while game_on:
    answer = turtle.textinput(title=title_prompt, prompt="What's another states name? ").title()
    if answer in states_list:
        count += 1
        index_of_state = states_list.index(answer)
        name_state = State_name(answer,x_coordinates_list[index_of_state],y_coordinates_list[index_of_state])
        title_prompt = f"{count}/{len(states_list)}"
    if count == total:
        game_on = False

screen.mainloop()

