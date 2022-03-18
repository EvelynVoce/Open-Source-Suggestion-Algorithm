import tkinter as tk


class Filters:

    def __init__(self):
        self.horror: bool = tk.BooleanVar()
        self.romance: bool = tk.BooleanVar()
        self.action: bool = tk.BooleanVar()

    def get_filters(self) -> list[str]:
        filters_names: list[str] = ["Horror", "Romance", "Action"]
        filters_list: list[bool] = [self.horror.get(), self.romance.get(), self.action.get()]
        return [name for name, bool_val in zip(filters_names, filters_list) if bool_val]


def filters(root, filter_obj):
    tk.Checkbutton(root, text="Horror", variable=filter_obj.horror).place(relx=0.70, rely=0.45)
    tk.Checkbutton(root, text="Romance", variable=filter_obj.romance).place(relx=0.70, rely=0.55)
