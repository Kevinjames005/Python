from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    is_it_empty = True
    if len(website_entry.get())== 0 or len(email_entry.get()) == 0 or len(password_entry.get())==0:
        is_it_empty = False
        messagebox.showinfo(title="Oops" ,message="Please make sure you haven't left any fields empty.")
    if is_it_empty:
        is_it_ok = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"These are the details that you entered: \n "
                                                                       f"email :{email_entry.get()} \n password:{password_entry.get()}\n"
                                                                       f"is it ok to save ?. ")
        if is_it_ok:
            with open(file="data.txt",mode="a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            website_entry.delete(0,END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file="logo.png")
image = canvas.create_image(100,100,image=lock_image)
canvas.grid(row=1,column=1)

website_label = Label(text="Website:")
website_label.grid(row=2,column=0,padx=5,pady=5,sticky="e")
website_entry = Entry(width=51)
website_entry.focus()
website_entry.grid(row=2,column=1,columnspan=2,padx=5,pady=5,sticky="w")

email_label = Label(text="email/username:")
email_label.grid(row=3,column=0,padx=5,pady=5,sticky="e")
email_entry = Entry(width=51)
email_entry.insert(0,"kevin@gmail.com")
email_entry.grid(row=3,column=1,columnspan=2,padx=5,pady=5,sticky="w")

password_label = Label(text="password:")
password_label.grid(row=4,column=0,padx=5,pady=5,sticky="e")
password_entry = Entry(width=30)
password_entry.grid(row=4,column=1,columnspan=1,padx=5,pady=5,sticky="w")

generate_button = Button(text="Generate Password",width=14)
generate_button.grid(row=4,column=2,padx=5,pady=5,sticky="w")

add_button = Button(text="add",width=43,command=save)
add_button.grid(row=5,column=1,columnspan=2,padx=5,pady=5,sticky="w")





window.mainloop()