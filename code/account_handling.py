import os
import csv
import Password_validation
from tkinter import messagebox
from utility import hashing, clear_root

script_dir = os.path.dirname(__file__)  # Script directory
script_dir, _ = script_dir.rsplit('\\', 1)  # Won't run correctly when running this file but will when running main
accounts_file_path = os.path.join(script_dir, 'user_data.csv')


def writing_account(signup_username, signup_password):
    if os.path.isfile(accounts_file_path):  # If the file exists, append new account to the file
        with open(accounts_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([signup_username, signup_password])

    else:  # If the file doesn't exist, create the file
        with open(accounts_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Password", "Viewed items"])
            writer.writerow([signup_username, signup_password])


def create_account(root, go_back, signup_username: str, signup_password: str):
    checks_passed: bool = Password_validation.run_checks(signup_password)  # Password validation
    if checks_passed:
        hashed_password: str = hashing(signup_password)
        writing_account(signup_username, hashed_password)
        messagebox.showinfo(message="Account created")
        clear_root(root)
        go_back()

    else:
        messagebox.showinfo(message="ERROR: Password invalid")


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
    if not likes_to_save:
        quit()

    with open(accounts_file_path, 'r', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        for row in reader:
            print(account)
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