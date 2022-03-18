import tkinter as tk
import utility
from account_handling import create_account

bg_col: str = "grey"
fg_col: str = "white"
button_col: str = "dark grey"


def signup_screen(root, func):
    signup_title = tk.Label(root, text="VMedia: Signup", font=("arial", 28, "bold"), fg=fg_col, bg=bg_col)
    signup_title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    utility.underline(signup_title)

    back_button = utility.create_back_button(root)
    back_button.config(command=lambda: utility.clear_root(root) or func())

    username_label = tk.Label(root, text="Username:", font=("arial", 15, "bold"), fg=fg_col, bg=bg_col)
    username_label.place(relx=0.05, rely=0.25)
    signup_username_entry = tk.Entry(root, relief=tk.GROOVE, bd=2, font=("arial", 13))
    signup_username_entry.place(relx=0.20, rely=0.25, relwidth=0.2, relheight=0.05)

    password_label = tk.Label(root, text="Password:", font=("arial", 15, "bold"), fg=fg_col, bg=bg_col)
    password_label.place(relx=0.05, rely=0.35)

    signup_password_entry = utility.PasswordField(root)
    signup_show = tk.Button(root, command=lambda: signup_password_entry.switch(), fg=fg_col, bg=bg_col)
    signup_show.place(relx=0.41, rely=0.35, relwidth=0.025, relheight=0.05)

    submit_details = tk.Button(root, text="signup", font=("arial", 10, "bold"),
                               bg=button_col, command=lambda:
                               create_account(root, func, signup_username_entry.get(),
                                              signup_password_entry.password_entry.get()))
    submit_details.place(relx=0.20, rely=0.75, relwidth=0.2, relheight=0.05)
