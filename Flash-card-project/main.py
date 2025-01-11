from tkinter import *
#-------------------------------------------Constants-----------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
#------------------------------------------UI setup------------------------------------------#
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

canvas = Canvas(width=800,height=526,highlightthickness=0)
white_image = PhotoImage(file="./images/card_front.png")
front_image = canvas.create_image(400,263,image=white_image)
canvas.grid(row=0,column=0)

window.mainloop()

