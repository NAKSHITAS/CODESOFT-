import random
import pyperclip
from tkinter import Tk, Label, Entry, IntVar, Checkbutton, Button, font


window = Tk()
window.title("Password Generator")


font_style = font.Font(family="Arial", size=10)


password_length_label = Label(
    window, text="Password Length:", font=font_style, pady=5
)
password_length_label.grid(row=0, column=0, sticky="W")  

password_length_entry = Entry(window, width=18, borderwidth=2, relief="solid")
password_length_entry.grid(row=0, column=1, padx=5, pady=5)  

# Checkboxes for character sets
char_types = {
    "lowercase": IntVar(value=1),
    "uppercase": IntVar(value=1),
    "numbers": IntVar(value=1),
    "symbols": IntVar(value=0),
}
for name, var in char_types.items():
    checkbox = Checkbutton(
        window, text=name.capitalize(), variable=var, font=font_style
    )
    checkbox.grid(row=1, column=list(char_types.keys()).index(name), sticky="W")


def generate_password():
    try:
        length = int(password_length_entry.get())
        char_set = ""
        for name, var in char_types.items():
            if var.get() and name not in char_set:
                if name == "lowercase":
                    char_set += "abcdefghijklmnopqrstuvwxyz"
                elif name == "uppercase":
                    char_set += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                elif name == "numbers":
                    char_set += "0123456789"
                else:
                    char_set += "!@#$%^&*()_-+={}[]|\:;'<,>.?/"
        password = ''.join(random.choices(char_set, k=length))
        password_display.config(text=password)
    except ValueError:
        password_display.config(text="Invalid Length Input")

generate_button = Button(
    window, text="Generate Password", command=generate_password, font=font_style
)
generate_button.grid(row=2, columnspan=2, pady=10)

# Label to display generated password
password_label = Label(window, text="Generated Password:", font=font_style, pady=5)
password_label.grid(row=3, column=0, sticky="W")

password_display = Label(window, text="")
password_display.grid(row=3, column=1, padx=5, pady=5)  # Add padding

# Button to copy password to clipboard (optional)
def copy_password():
    password = password_display.cget("text")
    if password:
        pyperclip.copy(password)

copy_button = Button(
    window, text="Copy to Clipboard", command=copy_password, font=font_style
)
copy_button.grid(row=4, columnspan=2, pady=5)


window.mainloop()
