from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def search_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            email_of_search_result = data[website]["email"]
            password_of_search_result = data[website]["password"]
            messagebox.showinfo(title=website,message=f"email:{email_of_search_result}\npassword:{password_of_search_result}")
    except FileNotFoundError:
        messagebox.showwarning(title="error",message="No data file found")
    except KeyError:
        messagebox.showwarning(title="error",message="no details for website exists")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }
    #print(new_data)
    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="error",message="no fields are to be empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"email:{email}\npassword:{password}\n")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)



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
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()
search_password = Button(text="Search password",command=search_password)
search_password.grid(row=1,column=2)

email_label = Label(text="email/username: ")
email_label.grid(row=2,column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"suriyaganesh97@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=3,column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password = Button(text="Generate password",command=generate_password)
generate_password.grid(row=3,column=2)

add_password = Button(text="Add password",width=36,command=save)
add_password.grid(row=4,column=1,columnspan=2)

window.mainloop()