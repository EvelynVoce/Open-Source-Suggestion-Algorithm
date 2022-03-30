from tkinter import font
import tkinter as tk
import hashlib


def underline(label):
    f = font.Font(label, label.cget("font"))  # Create custom font
    f.configure(underline=True)  # Underline font
    label.configure(font=f)  # Apply font to the given label


def close_app(root):
    root.destroy()


def clear_root(root):
    for ele in root.winfo_children():
        ele.destroy()


def create_back_button(root) -> tk.Button:
    button_col: str = "dark grey"
    back_button = tk.Button(root, text="back", font=("arial", 10, "bold"), bg=button_col)
    back_button.place(relx=0.90, rely=0.05, relwidth=0.1, relheight=0.05, anchor=tk.CENTER)
    return back_button


def hashing(data_to_encrypt) -> str:
    SALT: str = "AbX2f8Z&1SVFHUB4UZPW"
    plus_salt: str = data_to_encrypt + SALT
    hashed_data: str = hashlib.sha256(plus_salt.encode()).hexdigest()
    return hashed_data


class PasswordField:
    def __init__(self, root):
        self.asterisks: bool = True
        self.password_entry = tk.Entry(root, relief=tk.GROOVE, bd=2, font=("arial", 13), show="*")
        self.password_entry.place(relx=0.20, rely=0.35, relwidth=0.2, relheight=0.05)

    def switch(self):  # Gets the data for each media the user has liked
        if self.asterisks:
            self.password_entry.config(show="")
            self.asterisks = False
        else:
            self.password_entry.config(show="*")
            self.asterisks = True
