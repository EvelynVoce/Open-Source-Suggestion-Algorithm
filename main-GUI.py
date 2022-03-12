import tkinter as tk
import utility
from table_management import create_table

bg_col: str = "grey"
fg_col: str = "white"
button_col: str = "dark grey"

root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-5+0")
root.title("VMedia")
root.config(bg=bg_col)


def suggestion_gui(root):
    title = tk.Label(root, text="VMedia: Suggestions", font=("arial", 28, "bold"), fg=fg_col, bg=bg_col)
    title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    utility.underline(title)

    table = create_table(root)
    scroll_bar_y = tk.Scrollbar(root, command=table.yview)
    scroll_bar_y.place(relx=0.9, rely=0.15, relheight=0.8)


if __name__ == "__main__":
    suggestion_gui(root)
    root.mainloop()

