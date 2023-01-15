import tkinter as tk
from tkinter import messagebox
import pandas, pyperclip, json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint, choice, shuffle
def generate():

    charactors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    symbles = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

    numbers = ["1","2","3","4","5","6","7","8","9","0"]

    generated_password_charactors = [choice(charactors) for _ in range(0, 10)]
    generated_password_symbles = [choice(symbles) for _ in range(0, 5)]
    generated_password_numbers = [choice(numbers)  for _ in range(0, 3)]
    
    generated_passowrd = generated_password_charactors + generated_password_numbers +generated_password_symbles
    shuffle(generated_passowrd)
    generated_passowrd_shuffled = ''.join(generated_passowrd)

    password_input.insert(0,generated_passowrd_shuffled)
    pyperclip.copy(generated_passowrd_shuffled)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    if website_input.get() == "" or password_input.get() == "":
        messagebox.showinfo("Empty Field Detected", "You have left an empty input. Please make sure that all inputs are given.")
    else:
        is_ok = messagebox.askyesnocancel(website_input.get(), f"These are the details that you enter.\nWebsitename: {website_input.get()}\nPassword: {password_input.get()}\nIs these are right? ")
        new_data = {
            website_input.get():{
                "Email/Username" : Email_Username_input.get(),
                "Password" : password_input.get()
            }
        }
        if is_ok:
            try:
                with open("data.json", "r") as dataFile:
                    data = json.load(dataFile)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as writeData:
                    json.dump(new_data,writeData, indent=4)
            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as writeData:
                    json.dump(new_data,writeData, indent=4)
            else:
                with open("data.json", "w") as writeData:
                    json.dump(data,writeData, indent=4)
            finally:
                website_input.delete(0,"end") 
                password_input.delete(0,"end")
                website_input.focus()

# ---------------------------- SEARCH PASSWORD ---------------------------------- #
def searchPassword():
    try:
        website = website_input.get()
        with open("data.json", "r") as dataFile:
            data = json.load(dataFile)
            email = data[website]["Email/Username"]
            password = data[website]["Password"]
    except FileNotFoundError:
        messagebox.showerror(title="File", message="Password Manager File not found.")
    except KeyError:
        messagebox.showerror(title=website, message=f"This website is found.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassowrd: {password}")
    finally:
        website_input.delete(0,"end") 
        password_input.delete(0,"end")
        website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo 
canvass = tk.Canvas(width=200, height=200, highlightthickness=0)
image_path = tk.PhotoImage(file="logo.png")
canvass.create_image(100,100,image=image_path)
canvass.grid(column=2, row=1)

# Website Name
website = tk.Label(text="Website")
website.grid(column=1, row=2)

# Email_Username Name
Email_Username = tk.Label(text="Email/Username")
Email_Username.grid(column=1, row=3)

# Password Name
password = tk.Label(text="Password")
password.grid(column=1, row=4)

# Wensite Input
website_input = tk.Entry(width=21)
website_input.focus()
website_input.grid(column=2, row=2)

# Search Button
search_button = tk.Button(text="Search Password", command=searchPassword)
search_button.grid(column=3, row=2)

# Email_Username Input
Email_Username_input = tk.Entry(width=35)
Email_Username_input.insert(0, "mudassirameen104@gmail.com")
Email_Username_input.grid(column=2, row=3, columnspan=2)

# password Input
password_input = tk.Entry(width=21)
password_input.grid(column=2, row=4)

# Generate Button
generate = tk.Button(text="Generate Password", command=generate)
generate.grid(column=3, row=4)

# Add Button
add_button = tk.Button(text="ADD", width=36, command=save)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()