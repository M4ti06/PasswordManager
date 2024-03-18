import tkinter
import os
from tkinter import messagebox
import random
import pyperclip

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
    path = "./data.txt"
    str_website = website_entry.get()
    str_email = email_username_entry.get()
    str_password = password_entry.get()

    if len(str_website) == 0 or len(str_email) == 0 or len(str_password) == 0:
        messagebox.showerror(message="Plz provide missing data")
    else:
        is_ok = messagebox.askokcancel(message=f"Do you want to save this data?\n Website: {str_website}, "
                                               f"Email: {str_email}, Password: {str_password}")

        if is_ok:
            if os.path.isfile(path):
                with open("data.txt", "a") as file:
                    file.write(f"{str_website}||{str_email}||{str_password}\n")
            else:
                with open("data.txt", "a") as file:
                    file.write(f"{str_website}||{str_email}||{str_password}\n")
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            messagebox.showinfo(message="Password Saved")
# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.config( padx=20, pady=20)
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
website_entry.grid(column=1, row=1, columnspan=2)
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

window.mainloop()