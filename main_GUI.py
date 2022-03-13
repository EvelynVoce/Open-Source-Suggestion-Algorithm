import tkinter as tk
import utility
from table_management import create_table, insert_media_table
from media_data_csv_reader import reading_csv
from suggestion_algorithm2 import main_algorithm, suggestion_algorithm_single_use

bg_col: str = "grey"
fg_col: str = "white"
button_col: str = "dark grey"


def suggestion_gui(root, account_data):
    utility.clear_root(root)
    title = tk.Label(root, text="VMedia: Suggestions", font=("arial", 28, "bold"), fg=fg_col, bg=bg_col)
    title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    utility.underline(title)

    table = create_table(root)
    scroll_bar_y = tk.Scrollbar(root, command=table.yview)
    scroll_bar_y.place(relx=0.9, rely=0.15, relheight=0.8)

    # A second list is made so media already used to calculate score do not need to be checked again
    print(f"{account_data=}")
    likes_to_save: list[int] = [int(x) for x in account_data]

    list_of_media_classes = reading_csv()  # 0.1 seconds roughly
    print(len(list_of_media_classes))
    media_data_to_set_scores = suggestion_algorithm_single_use(list_of_media_classes, likes_to_save)

    ordered_media_classes = main_algorithm(list_of_media_classes, media_data_to_set_scores, likes_to_save)

    insert_media_table(table, ordered_media_classes)


# if __name__ == "__main__":
#     suggestion_gui(root)
#     root.mainloop()

