from tkinter import *

window = Tk()
window.title("Miles to Km")
window.config(padx=20,pady=20)

blank_label = Label()
blank_label.grid(row=0,column=0)

input = Entry(width = 10)
input.insert(END , string="0")
input.grid(row=0,column=1)

miles_label = Label(text = "miles")
miles_label.grid(row=0,column=2)
kilometers = 0
equal_to_label = Label(text = "is equal to")
equal_to_label.grid(row=1,column=0)

kilometers_label = Label(text = "0")
kilometers_label.grid(row=1,column=1)

km_label = Label(text = "km")
km_label.grid(row=1,column=2)

def calc():
    miles = float(input.get())
    km = miles * 1.609
    round_km = round(km,2)
    kilometers_label.config(text=f"{round_km}")

calculate = Button(text="calculate" , command=calc)
calculate.grid(row=2,column=1)



window.mainloop()