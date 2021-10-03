from tkinter import *
import pandas
from random import *

df = pandas.read_csv("data/french_words.csv")
dict_file = df.to_dict(orient="records")

window = Tk()
window.title("Flashcard")
window.config(padx="50",pady="50")

def change_name():
    word_to_learn = choice(dict_file)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=choice(dict_file)["French"])

canvas = Canvas(width="800",height="526")
canvas.config(bg="#9bdeac",highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=front_image)
card_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="name",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)



wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,command=change_name)
wrong_button.grid(row=1,column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,command=change_name)
right_button.grid(row=1,column=1)

change_name()
window.mainloop()