import tkinter as tk


class Filters:

    def __init__(self):
        self.horror: bool = tk.BooleanVar()
        self.romance: bool = tk.BooleanVar()
        self.action: bool = tk.BooleanVar()
        self.crime: bool = tk.BooleanVar()
        self.drama: bool = tk.BooleanVar()
        self.thriller: bool = tk.BooleanVar()
        self.sci_fi: bool = tk.BooleanVar()
        self.fantasy: bool = tk.BooleanVar()

    def get_filters(self) -> list[str]:
        filters_names: list[str] = ["Horror", "Romance", "Action", "Crime", "Drama", "Thriller", "Sci-Fi", "Fantasy"]
        filters_list: list[bool] = [self.horror.get(), self.romance.get(),
                                    self.action.get(), self.crime.get(),
                                    self.drama.get(), self.thriller.get(),
                                    self.sci_fi.get(), self.fantasy.get()]
        return [name for name, bool_val in zip(filters_names, filters_list) if bool_val]


def filters(root, filter_obj):
    tk.Checkbutton(root, text="Horror", font=("arial", 15), variable=filter_obj.horror).place(relx=0.60, rely=0.30)
    tk.Checkbutton(root, text="Action", font=("arial", 15), variable=filter_obj.action).place(relx=0.65, rely=0.30)

    tk.Checkbutton(root, text="Romance", font=("arial", 15), variable=filter_obj.romance).place(relx=0.60, rely=0.35)
    tk.Checkbutton(root, text="Crime", font=("arial", 15), variable=filter_obj.crime).place(relx=0.65, rely=0.35)

    tk.Checkbutton(root, text="Drama", font=("arial", 15), variable=filter_obj.drama).place(relx=0.60, rely=0.40)
    tk.Checkbutton(root, text="Sci-Fi", font=("arial", 15), variable=filter_obj.sci_fi).place(relx=0.65, rely=0.40)

    tk.Checkbutton(root, text="Thriller", font=("arial", 15), variable=filter_obj.thriller).place(relx=0.60, rely=0.45)
    tk.Checkbutton(root, text="Fantasy", font=("arial", 15), variable=filter_obj.fantasy).place(relx=0.65, rely=0.45)
