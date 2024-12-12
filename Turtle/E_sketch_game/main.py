import turtle as t

tim = t.Turtle()
screen = t.Screen()

def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def turn_clockwise():
    tim.right(10)
def turn_counter_clockwise():
    tim.left(10)

def clear_screen():
    screen.resetscreen()


screen.listen()
screen.onkeypress(key = "w" , fun = forward)
screen.onkey(key = "s" , fun = backward)
screen.onkeypress(key = "d" , fun = turn_clockwise)
screen.onkeypress(key = "a" , fun = turn_counter_clockwise)
screen.onkey(key = "c" , fun = clear_screen)
screen.exitonclick()