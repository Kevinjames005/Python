import random
from tkinter import *
import pandas
#-------------------------------------------Constants-----------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
random_key=None
#------------------------------------------Read File------------------------------------------#
data = pandas.read_csv("./data/french_words.csv")
data_dict = dict(zip(data['French'], data['English']))
#------------------------------------------Random Words------------------------------------------#

def random_key_fun():
    global random_key
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(front_image,image=new_image)
    random_key = random.choice(list(data_dict.keys()))
    canvas.itemconfig(title_word,text="French",fill="black")
    canvas.itemconfig(word_meaning,text=f"{random_key}",fill="black")
    flip_timer = window.after(3000,random_value_fun)

def random_value_fun():
    global random_key,green_image
    random_value = data_dict[random_key]
    canvas.itemconfig(front_image,image=green_image)
    canvas.itemconfig(title_word,text="English",fill="white")
    canvas.itemconfig(word_meaning,text=f"{random_value}",fill="white")
#-----------------------------------------Save File------------------------------------------#


#------------------------------------------UI setup------------------------------------------#
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer = window.after(3000,random_value_fun)
canvas = Canvas(width=800,height=526,highlightthickness=0)
white_image = PhotoImage(file="./images/card_front.png")
new_image = PhotoImage(file="./images/card_front.png")
green_image = PhotoImage(file="./images/card_back.png")
front_image = canvas.create_image(400,263,image=white_image)
title_word = canvas.create_text(400,150,text="French",font=("Arial",30,"italic"))
word_meaning = canvas.create_text(400,300,text="Word",font=("Arial",40,"bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0,columnspan=2)


wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=random_key_fun)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=random_key_fun)
right_button.grid(row=1,column=1)

random_key_fun()

window.mainloop()

