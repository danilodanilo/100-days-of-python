from tkinter import *
from tkinter import messagebox
import re
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # using list comprehension
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password_input.get())
    #print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def validate_email(email):
    # Make a regular expression
    # for validating an Email

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True

    else:
        return False


def save_password():
    website_input_value = website_input.get()
    email_input_value = email_username_input.get()
    password_input_value = password_input.get()

    if website_input_value == "":
        messagebox.showerror(title="Website", message="Please, provide a Website value")
        website_input.focus()
    elif email_input_value == "":
        messagebox.showerror(title="Email", message="Please, provide an Email")
        email_username_input.focus()
    elif password_input_value == "":
        messagebox.showerror(title="Password", message="Please, provide a Password")
        password_input.focus()
    else:
        if not validate_email(email_input_value):
            messagebox.showerror(title="Invalid Email", message="Please, provide a valid Email")
            email_username_input.focus()
        else:
            if messagebox.askokcancel(title="Confirm the information",
                                      message=f"There are the details you entered: \n Website: {website_input_value}\n "
                                              f"Email: {email_input_value}\n Password: {password_input_value}. Do you "
                                              f"wish to proceed?"):
                with open("file.txt", "a") as file:
                    file.write(website_input_value + " | " + email_input_value + " | " + password_input_value + "\n")
                    website_input.delete(0, 'end')
                    email_username_input.delete(0, 'end')
                    password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
bg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg)
canvas.grid(row=0, column=1)

# labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2)
button_add = Button(text="Add", width=36, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
