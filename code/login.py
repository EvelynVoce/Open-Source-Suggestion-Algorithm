import tkinter as tk
import utility
import csv
import os
from tkinter import messagebox
import main_GUI

bg_col: str = "grey"
fg_col: str = "white"
button_col: str = "dark grey"

script_dir = os.path.dirname(__file__)  # Script directory
script_dir, _ = script_dir.rsplit('\\', 1)  # Won't run correctly when running this file but will when running main
accounts_file_path = os.path.join(script_dir, 'user_data.csv')


def reading_account(login_username, login_password):
    if os.path.isfile(accounts_file_path):
        with open(accounts_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')  # Read each line of the user_data csv
            next(csv_reader)  # Skip the first line because it's just the headings for the columns
            for row in csv_reader:
                if row[0] == login_username and row[1] == login_password:
                    return row


def updating_account_data(account, likes_to_save):
    lines_to_write_back = []

    # Updates the current user account data
    with open(accounts_file_path, 'r', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] == account[0] and row[1] == account[1]:
                string_of_likes = ""
                for like in range(len(likes_to_save) - 1):
                    string_of_likes += str(likes_to_save[like]) + ","
                string_of_likes += str(likes_to_save[-1])
                lines_to_write_back.append((row[0], row[1], string_of_likes))
            else:
                lines_to_write_back.append(row)

    # Writes all data, including updated user data, back to the accounts file
    with open(accounts_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for line in lines_to_write_back:
            try:  # This is needed because some users may have no likes yet
                data = line[2]
            except IndexError:
                data = ""
            writer.writerow([line[0], line[1], data])
    quit()


def login_account(root, login_username, login_password):
    account_found = reading_account(login_username, utility.hashing(login_password))
    if account_found is not None:
        try:
            print(account_found)
            account_data = account_found[2].split(',')
        except IndexError:
            account_data = []  # If the account is new it will have no data associated with it

        likes_to_save = main_GUI.suggestion_gui(root, account_data)

        # If suggestion_algorithm is exited it means the program is ready to close
        print("UPDATING ACCOUNT DATA")
        updating_account_data(account_found, likes_to_save)
    else:
        messagebox.showinfo(message="ERROR: Invalid account details")


def login_screen(root, func):
    login_title = tk.Label(root, text="VMedia: login", font=("arial", 28, "bold"), fg=fg_col, bg=bg_col)
    login_title.place(relx=0.50, rely=0.05, anchor=tk.CENTER)
    utility.underline(login_title)

    back_button = utility.create_back_button(root)
    back_button.config(command=lambda: utility.clear_root(root) or func())

    username_label = tk.Label(root, text="Username:", font=("arial", 15, "bold"), fg=fg_col, bg=bg_col)
    username_label.place(relx=0.05, rely=0.25)
    password_label = tk.Label(root, text="Password:", font=("arial", 15, "bold"), fg=fg_col, bg=bg_col)
    password_label.place(relx=0.05, rely=0.35)

    username_entry = tk.Entry(root, relief=tk.GROOVE, bd=2, font=("arial", 13))
    username_entry.place(relx=0.20, rely=0.25, relwidth=0.2, relheight=0.05)

    login_password_entry = utility.PasswordField(root)
    login_show = tk.Button(root, command=lambda: login_password_entry.switch(), fg=fg_col, bg=bg_col)
    login_show.place(relx=0.41, rely=0.35, relwidth=0.025, relheight=0.05)
    login_submission = tk.Button(root, text="login", font=("arial", 10, "bold"),
                                 bg=button_col, command=lambda:
                                 login_account(root, username_entry.get(), login_password_entry.password_entry.get()))
    login_submission.place(relx=0.20, rely=0.65, relwidth=0.28, relheight=0.1)
