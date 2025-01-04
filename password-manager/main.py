from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file="logo.png")
image = canvas.create_image(100,100,image=lock_image)
canvas.grid(row=1,column=1)

website_label = Label(text="Website:")
website_label.grid(row=2,column=0)
website_entry = Entry(width=40)
website_entry.grid(row=2,column=1,columnspan=2)

email_label = Label(text="email/username:")
email_label.grid(row=3,column=0)
email_entry = Entry(width=40)
email_entry.grid(row=3,column=1,columnspan=2)

password_label = Label(text="password:")
password_label.grid(row=4,column=0)
password_entry = Entry(width=20)
password_entry.grid(row=4,column=1,columnspan=1)

generate_button = Button(text="Generate Password",width=10)
generate_button.grid(row=4,column=2)

add_button = Button(text="add",width=35)
add_button.grid(row=5,column=1,columnspan=2)





window.mainloop()