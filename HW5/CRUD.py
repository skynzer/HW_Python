import create_1
import read_1
import update_1
import delete_1
import sys
import argparse

user_emails = []
users_storage = {}

parser = argparse.ArgumentParser()
parser.add_argument('--Help', type=str)
arg = parser.parse_args()
call_help = True if arg.Help == "--Help" else False

if call_help:
    print("This is help")
else:
    while True:
        action = input("Please enter create or read, or update, or delete actions: \n")

        if action == "create":
            print("action =", action)
            email = input("Email: ")
            name = input("Name: ")
            password = input("Password: ")
            phone = input("Phone: ")
            create_1.create_user(email, name, password, phone, user_emails, users_storage)
            print(user_emails)
            print("storage", users_storage)
        elif action == "read_all":
            print(read_1.all_user_info(users_storage))
        elif action == "read_user":
            email = input("Enter user email: ")
            print(read_1.read_user_info(email, user_emails, users_storage))
        elif action == "update_user":
            email = input("Enter user email: ")
            print(update_1.update(email, user_emails, users_storage))
        elif action == "delete":
            email = input("Input email of user whom you want to delete t or all to delete all users: ")
            print(delete_1.delete(email, user_emails, users_storage))
        else:
            print("Please enter create or read, or update, or delete actions:")
