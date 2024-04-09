import json
import random
from tkinter import *
from tkinter import messagebox
import string
import pyperclip
from random import choice, randint

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = list(string.ascii_letters)
    numbers = [str(num) for num in range(0, 9)]
    symbols = ['!', '@', '#', '$', '%', '&', '*']

    password_letters = [choice(letters) for _ in range(randint(0, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password_to_file():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}
    if not website or not email or not password:
        messagebox.showerror("Invalid Input(s)", "Please fill in all fields before trying to save")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_password():
    target_website = website_entry.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("There are no saved passwords :(")
    else:
        if target_website in data:
            email = data[target_website]["email"]
            password = data[target_website]["password"]
            messagebox.showinfo(f"Login Info for {target_website}:\nEmail/Username: {email}\nPassword: {password}")
        else:
            messagebox.showerror(f"No passwords found for {target_website}")
# ---------------------------- UI SETUP ------------------------------- #


app = Tk()
app.title("Password Manager")
app.config(padx=50, pady=50)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# website
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)

# Username or email
user_label = Label(text="Username/Email")
user_label.grid(column=0, row=2)

user_entry = Entry(width=41)
user_entry.insert(END, "filler@email.com")
user_entry.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add", width=36, command=save_password_to_file)
add_password_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search_password, width=13)
search_button.grid(column=2, row=1)


# Mainloop
app.mainloop()
