from tkinter import *
import pandas
from random import *

df = pandas.read_csv("data/french_words.csv")
dict_file = df.to_dict(orient="records")
current_card = {}

def change_name():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(dict_file)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background,image=back_image)


def is_known():
    dict_file.remove(current_card)
    change_name()
    data = pandas.DataFrame(dict_file)
    data.to_csv("data/words_to_learn.csv",index=False)
    change_name()


window = Tk()
window.title("Flashcard")
window.config(padx="50",pady="50")
flip_timer = window.after(3000,func=flip_card)


canvas = Canvas(width="800",height="526")
canvas.config(bg="#9bdeac",highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=front_image)
card_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="name",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)



wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,command=change_name)
wrong_button.grid(row=1,column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,command=is_known)
right_button.grid(row=1,column=1)

change_name()
window.mainloop()