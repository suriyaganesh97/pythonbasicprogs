from tkinter import *

window = Tk()
window.title("milesToKm")
window.minsize(width=500, height=300)
window.config(padx=50, pady=100)

miles_input = Entry(width=10)
miles_input.grid(row=0,column=2)
miles_label = Label(text="miles")
miles_label.grid(row=0,column=3)

label = Label(text="is equal to")
label.grid(row=1,column=1)
km_value = Label(width=10,text="0")
km_value.grid(row=1,column=2)
km_label = Label(text="km")
km_label.grid(row=1,column=3)


def calc_km():
    miles = miles_input.get()
    km = float(miles) * 1.609
    km_value.config(text=km)


button = Button(text="calculate",command=calc_km)
button.grid(row=2,column=2)
mainloop()