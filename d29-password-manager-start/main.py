from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=password_image)
canvas.grid(row=0,column=1)

website_label = Label(text="website: ")
website_label.grid(row=1,column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_label = Label(text="email/username: ")
email_label.grid(row=2,column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"suriyaganesh97@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=3,column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password = Button(text="Generate password")
generate_password.grid(row=3,column=2)

add_password = Button(text="Add password",width=36,command=add_data)
add_password.grid(row=4,column=1,columnspan=2)







window.mainloop()