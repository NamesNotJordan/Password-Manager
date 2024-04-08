from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

app = Tk()
app.title("Password Manager")
app.config(padx=20, pady=20)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

#Label Input pairs
# website
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

# Username or email
user_label = Label(text="Username or Email")
user_label.grid(column=0, row=2)

# Password
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add")
add_password_button.grid(column=1, row=4)

# Mainloop
app.mainloop()