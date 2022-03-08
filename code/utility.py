from tkinter import font
import tkinter as tk


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
