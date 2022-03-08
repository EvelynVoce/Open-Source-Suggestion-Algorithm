from tkinter import font


def underline(label):
    f = font.Font(label, label.cget("font"))  # Create custom font
    f.configure(underline=True)  # Underline font
    label.configure(font=f)  # Apply font to the given label


def close_app(root):
    root.destroy()


def clear_root(root):
    for ele in root.winfo_children():
        ele.destroy()