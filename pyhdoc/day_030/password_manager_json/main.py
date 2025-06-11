# # Password Manager Project

import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generates a random password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = (
        [choice(letters) for _ in range(nr_letters)] +
        [choice(symbols) for _ in range(nr_symbols)] +
        [choice(numbers) for _ in range(nr_numbers)]
    )

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Saves the password and website into a file"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
   
    if is_ok:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1, sticky="w", padx=5, pady=5)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="w", padx=5, pady=5)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3, sticky="w", padx=5, pady=5)

# Entries
website_entry = tk.Entry(width=43)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew", padx=5, pady=5)
website_entry.focus()

email_entry = tk.Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5, pady=5)
email_entry.insert(0, "H2m0v@example.com")

password_entry = tk.Entry(width=25)
password_entry.grid(column=1, row=3, sticky="ew", padx=(5, 0), pady=5)

# Buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="ew", padx=(5, 10), pady=5)

add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=5, pady=10)



window.mainloop()