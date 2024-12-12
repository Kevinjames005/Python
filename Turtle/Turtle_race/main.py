from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title = "Make your bet" , prompt = "Which turtle will win in the race ? Enter a color :")
is_race_on = False
all_turtles =[]
colors = ["red" ,"orange" , "yellow" ,  "green"  , "blue" , "purple"]

y = -100
for i in range(6):
    all_turtles.append(Turtle(shape="turtle"))
    all_turtles[i].penup()
    all_turtles[i].color(colors[i])
    all_turtles[i].goto(x = -220 , y = y)
    y += 40
if user_bet:
    is_race_on = True

while is_race_on:
    for tim in all_turtles:
        if tim.xcor() > 230:
            is_race_on = False
            if tim.pencolor() == user_bet:
                print(f"{tim.pencolor()} won the race and You've won the bet.")
            else :
                print(f"{tim.pencolor()} won the race and You've lose the bet.")

        random_distance = random.randint(0 ,10)
        tim.forward(random_distance)


screen.exitonclick()






