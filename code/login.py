import tkinter as tk
import utility
from account_handling import reading_account
from tkinter import messagebox
import main_GUI

bg_col: str = "grey"
fg_col: str = "white"
button_col: str = "dark grey"


def login_account(root, login_username, login_password):
    account_found = reading_account(login_username, utility.hashing(login_password))
    if account_found is not None:
        try:
            account_data = account_found[2].split(',')
        except IndexError:
            account_data = []  # If the account is new it will have no data associated with it

        main_GUI.suggestion_gui(root, account_data, account_found)
    else:
        messagebox.showinfo(message="ERROR: Invalid account details")


def login_screen(root, func):
    login_title = tk.Label(root, text="VMedia: login", font=("arial", 28, "bold"), fg=fg_col, bg=bg_col)
    login_title.place(relx=0.50, rely=0.05, anchor=tk.CENTER)
    utility.underline(login_title)

    back_button = utility.create_back_button(root)
    back_button.config(command=lambda: utility.clear_root(root) or func())

    username_label = tk.Label(root, text="Username:", font=("arial", 15, "bold"), fg=fg_col, bg=bg_col)
    username_label.place(relx=0.05, rely=0.25)
    password_label = tk.Label(root, text="Password:", font=("arial", 15, "bold"), fg=fg_col, bg=bg_col)
    password_label.place(relx=0.05, rely=0.35)

    username_entry = tk.Entry(root, relief=tk.GROOVE, bd=2, font=("arial", 13))
    username_entry.place(relx=0.20, rely=0.25, relwidth=0.2, relheight=0.05)

    login_password_entry = utility.PasswordField(root)
    login_show = tk.Button(root, command=lambda: login_password_entry.switch(), fg=fg_col, bg=bg_col)
    login_show.place(relx=0.41, rely=0.35, relwidth=0.025, relheight=0.05)
    login_submission = tk.Button(root, text="login", font=("arial", 10, "bold"),
                                 bg=button_col, command=lambda:
                                 login_account(root, username_entry.get(), login_password_entry.password_entry.get()))
    login_submission.place(relx=0.20, rely=0.65, relwidth=0.28, relheight=0.1)
