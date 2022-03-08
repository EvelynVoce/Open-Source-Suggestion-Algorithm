import tkinter as tk
import utility
from signup import signup_screen

bg_col: str = "grey"
fg_col: str = "white"
button_col: str = "dark grey"

root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-5+0")
root.title("VMedia")
root.config(bg=bg_col)

root.bind('<Escape>', lambda event: utility.close_app(root))


def login_screen():
    print("Login")


def main_screen():
    welcoming = tk.Label(root, text="VMedia", font=("arial", 28, "bold"), fg=fg_col, bg=bg_col)
    welcoming.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    utility.underline(welcoming)

    login_button = tk.Button(root, text="login", font=("arial", 10, "bold"),
                             bg=button_col, command=lambda: utility.clear_root(root) or login_screen())
    login_button.place(relx=0.25, rely=0.35, relwidth=0.2, relheight=0.1)

    signup_button = tk.Button(root, text="signup", font=("arial", 10, "bold"),
                              bg=button_col, command=lambda: utility.clear_root(root)
                              or signup_screen(root, main_screen))
    signup_button.place(relx=0.55, rely=0.35, relwidth=0.2, relheight=0.1)


if __name__ == "__main__":
    main_screen()
    root.mainloop()

