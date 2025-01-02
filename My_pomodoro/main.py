import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#2E5077"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps == 8 :
        count_down(long_break)
        timer_label.config(text="Break" , fg="white")
    elif reps %2 == 0 :
        count_down(work_min)
        timer_label.config(text="Work", fg="white")
    else :
        count_down(short_break)
        timer_label.config(text="Break", fg="white")
    reps += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10 :
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else :
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        tick_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg=BLUE)

timer_label=Label(text="Timer",fg="white",bg=BLUE,font=(FONT_NAME,50,"normal"))
timer_label.grid(row=0,column=1)

canvas = Canvas(width=224,height=224,bg=BLUE,highlightthickness=0)
tomato_img = PhotoImage(file="lunar_surface image.png")
canvas.create_image(112,112,image=tomato_img)
timer_text = canvas.create_text(112,112,text="00:00",fill="black",font=(FONT_NAME,40,"bold"))
canvas.grid(row=1,column=1)


start_button= Button(text="Start",command=start_timer)
start_button.grid(row = 2,column=0)

reset_button= Button(text="Reset" , command=reset_timer)
reset_button.grid(row = 2,column=3)

tick_label = Label(fg="white",bg=BLUE,font=(FONT_NAME,20,"normal"))
tick_label.grid(row=4,column=1)



window.mainloop()