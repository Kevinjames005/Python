import turtle
import pandas
from print_states import print_state

screen = turtle.Screen()
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)



answer = turtle.textinput(title = "Guess the states" , prompt="What's another states name? ").title()
data = pandas.read_csv("50_states.csv")
states = data.state
states_list = states.to_list()

if answer in states_list:
    x_cord = data.loc[data["state"] == answer, "x"]
    y_cord = data.loc[data["state"] == answer, "y"]
    x_point = x_cord[0]
    y_point = y_cord[0]

    print(x_point)


    name_state = print_state(answer , x_cord , y_cord)





screen.mainloop()

