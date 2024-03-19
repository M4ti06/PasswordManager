import tkinter
import os
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def search():
    str_website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            found_email = data[str_website]["email"]
            found_password = data[str_website]["password"]
            messagebox.showinfo(message=f"Yours email: {found_email} and password: {found_password}")
    except FileNotFoundError:
        messagebox.showerror(message="There is no passwords in the vault")
    except KeyError:
        messagebox.showerror(message="There is no such website in the vault")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for char in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = pass_numbers + pass_symbols + pass_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    path = "./data.json"
    str_website = website_entry.get()
    str_email = email_username_entry.get()
    str_password = password_entry.get()

    new_data = {
        str_website: {
            "email": str_email,
            "password": str_password,
    }
    }

    if len(str_website) == 0 or len(str_email) == 0 or len(str_password) == 0:
        messagebox.showerror(message="Plz provide missing data")
    else:
        is_ok = messagebox.askokcancel(message=f"Do you want to save this data?\n Website: {str_website}, "
                                               f"Email: {str_email}, Password: {str_password}")

        if is_ok:
            if os.path.isfile(path):
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            messagebox.showinfo(message="Password Saved")
# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.config( padx=50, pady=50)
window.title("PasswordManager")


canvas = tkinter.Canvas(width=200, height=200)
photo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website")
website_label.grid(column=0, row=1)

email_username_label = tkinter.Label(text="Email/Username")
email_username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_username_entry = tkinter.Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0,"1234@256.com")

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)

generate_pass_button = tkinter.Button( text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = tkinter.Button(width=21, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tkinter.Button(text="Search", width=21, command=search)
search_button.grid(column=2, row=1)
window.mainloop()