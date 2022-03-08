import tkinter as tk
import utility

bg_col: str = "grey"
fg_col: str = "white"
button_col: str = "dark grey"


def signup_screen(root, func):
    welcoming = tk.Label(root, text="Test Signup", font=("arial", 28, "bold"), fg=fg_col, bg=bg_col)
    welcoming.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    utility.underline(welcoming)

    signup_button = tk.Button(root, text="Back", font=("arial", 10, "bold"),
                              bg=button_col, command=lambda: utility.clear_root(root) or func())
    signup_button.place(relx=0.55, rely=0.35, relwidth=0.2, relheight=0.1)
