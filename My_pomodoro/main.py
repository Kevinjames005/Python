from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg=YELLOW)

timer_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"normal"))
timer_label.grid(row=0,column=1)

canvas = Canvas(width=202,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato_img)
canvas.create_text(102,132,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

start_button= Button(text="Start")
start_button.grid(row = 2,column=0)

reset_button= Button(text="Reset")
reset_button.grid(row = 2,column=3)

tick_label = Label(text="✓",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"normal"))
tick_label.grid(row=4,column=1)



window.mainloop()