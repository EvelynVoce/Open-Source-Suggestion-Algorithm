import tkinter as tk
import utility
from table_management import create_table, insert_media_table
from media_data_csv_reader import reading_csv
from suggestion_algorithm2 import main_algorithm, suggestion_algorithm_single_use, selecting_media
from main_and_accounts import updating_account_data

bg_col: str = "grey"
fg_col: str = "white"
button_col: str = "dark grey"

global_likes_to_save = []


def select_media(table, likes_to_save, list_of_media_classes):
    cur_item = table.focus()
    row_data: dict = table.item(cur_item)
    item_values: list = row_data['values']
    selected_title = item_values[0]
    media_selected, likes_to_save = selecting_media(likes_to_save, selected_title)
    global global_likes_to_save
    global_likes_to_save = likes_to_save
    selected_data = media_selected.data
    updating_gui(table, selected_data, likes_to_save, list_of_media_classes)


def clearing_table(table):
    for x in table.get_children():
        table.delete(x)


def updating_gui(table, media_data_to_set_scores, likes_to_save, list_of_media_classes):
    clearing_table(table)
    ordered_media_classes = main_algorithm(list_of_media_classes, media_data_to_set_scores, likes_to_save)
    insert_media_table(table, ordered_media_classes)


def search(table, list_of_media_classes, searched_item):
    clearing_table(table)
    matched_searches = [media for media in list_of_media_classes if searched_item in media.title]
    insert_media_table(table, matched_searches)


def suggestion_gui(root, account_data, account_found):
    print(f"{account_data = }")
    utility.clear_root(root)
    title = tk.Label(root, text="VMedia: Suggestions", font=("arial", 28, "bold"), fg=fg_col, bg=bg_col)
    title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    utility.underline(title)

    table = create_table(root)
    table.place(relx=0.1, rely=0.2, relwidth=0.80, relheight=0.75)
    scroll_bar_y = tk.Scrollbar(root, command=table.yview)
    scroll_bar_y.place(relx=0.9, rely=0.2, relheight=0.8)

    select_button = tk.Button(root, text="Select media", font=("arial", 10, "bold"),
                              bg=button_col, command=lambda: select_media(table, likes_to_save, list_of_media_classes))
    select_button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    search_bar = tk.Entry(root, relief=tk.GROOVE, bd=2, font=("arial", 13))
    search_bar.place(relx=0.1, rely=0.15, relwidth=0.68, relheight=0.025)

    search_button = tk.Button(root, text="Search", font=("arial", 10, "bold"),
                              bg=button_col, command=lambda: search(table, list_of_media_classes, search_bar.get()))
    search_button.place(relx=0.8, rely=0.15, relwidth=0.05, relheight=0.025)

    show_all_button = tk.Button(root, text="Show All", font=("arial", 10, "bold"),
                                bg=button_col, command=lambda: search(table, list_of_media_classes, ""))
    show_all_button.place(relx=0.86, rely=0.15, relwidth=0.05, relheight=0.025)

    exit_button = tk.Button(root, text="Exit", font=("arial", 10, "bold"),
                            bg=button_col, command=lambda: updating_account_data(account_found, likes_to_save))
    exit_button.place(relx=0.8, rely=0.05, relwidth=0.1, relheight=0.05)

    # A second list is made so media already used to calculate score do not need to be checked again
    if account_data == ['']:
        account_data = []
    likes_to_save: list[int] = [int(x) for x in account_data]
    global global_likes_to_save
    global_likes_to_save = likes_to_save

    list_of_media_classes = reading_csv()  # 0.1 seconds roughly
    print(len(list_of_media_classes))
    media_data_to_set_scores = suggestion_algorithm_single_use(list_of_media_classes, likes_to_save)

    ordered_media_classes = main_algorithm(list_of_media_classes, media_data_to_set_scores, likes_to_save)
    insert_media_table(table, ordered_media_classes)

