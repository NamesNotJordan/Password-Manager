from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password_to_file():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    with open("passwords.tx", "a") as file:
        file.write(f"{website}|{email}|{password}\n")
    website_entry.delete(0, END)
    password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


app = Tk()
app.title("Password Manager")
app.config(padx=50, pady=50)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

#Label Input pairs
# website
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")

# Username or email
user_label = Label(text="Username/Email")
user_label.grid(column=0, row=2)

user_entry = Entry(width=35)
user_entry.insert(END, "filler@email.com")
user_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

# Password
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add", width=36, command=save_password_to_file)
add_password_button.grid(column=1, row=4, columnspan=2)

# Mainloop
app.mainloop()