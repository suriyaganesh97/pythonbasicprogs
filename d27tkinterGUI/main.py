
from tkinter import *

window = Tk()
window.title("my first GUI project")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)   #padding added on the entire window same can be done for individual widgets as well


my_label = Label(text="i am a label", font=("Arial", 12, "bold"))
my_label.grid(row=0, column=0)


def button_clicked():
    user_text = input.get()
    my_label.config(text=user_text)


button = Button(text="click me", command=button_clicked)
button.grid(row=1, column=2)

new_button = Button(text="new button")
new_button.grid(row=0, column=4)

input = Entry(width=10)
input.grid(row=2, column=6)

mainloop()