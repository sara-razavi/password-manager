# Name: Sara Razavi
# Student ID: 970050118
# Project date: January 19,2020
# focus: dictionaries, lists, strings, random, files and functions

import random
import string

passwords = []

def make_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%"

    result = ""

    for i in range(length):
        result += random.choice(characters)

    return result

def add_password():
    website = input("Website: ").strip()
    username = input("Username: ").strip()

    length_text = input("Password length: ")

    if not length_text.isdigit():
        print("Enter a number.")
        return

    length = int(length_text)

    if length < 4:
        print("Password is too short for this exercise.")
        return

    password = make_password(length)

    item = {
        "website": website,
        "username": username,
        "password": password
    }

    passwords.append(item)

    print("Generated password:", password)
    print("Saved in the program.")

def show_all():
    print("\n--------- SAVED ACCOUNTS ---------")

    if len(passwords) == 0:
        print("Nothing saved.")
        return

    for i in range(len(passwords)):
        item = passwords[i]
        print(i + 1, item["website"], "-", item["username"])

def search_password():
    website = input("Search website: ").lower().strip()
    found = False

    for item in passwords:
        if item["website"].lower() == website:
            print("Website:", item["website"])
            print("Username:", item["username"])
            print("Password:", item["password"])
            found = True

    if not found:
        print("Nothing found.")

def delete_password():
    show_all()

    if len(passwords) == 0:
        return

    number = input("Number to delete: ")

    if number.isdigit():
        number = int(number)

        if 1 <= number <= len(passwords):
            passwords.pop(number - 1)
            print("Deleted.")
        else:
            print("Invalid number.")
    else:
        print("Enter a number.")

def save_passwords():
    file = open("passwords.txt", "w")

    for item in passwords:
        file.write(
            item["website"] + "|" +
            item["username"] + "|" +
            item["password"] + "\n"
        )

    file.close()

def load_passwords():
    try:
        file = open("passwords.txt", "r")

        for line in file:
            parts = line.strip().split("|")

            if len(parts) == 3:
                passwords.append({
                    "website": parts[0],
                    "username": parts[1],
                    "password": parts[2]
                })

        file.close()

    except FileNotFoundError:
        pass

load_passwords()

while True:
    print("\n============================")
    print("       PASSWORD NOTES")
    print("============================")
    print("1. Generate password")
    print("2. Show websites")
    print("3. Search")
    print("4. Delete")
    print("5. Save")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        show_all()
    elif choice == "3":
        search_password()
    elif choice == "4":
        delete_password()
    elif choice == "5":
        save_passwords()
        print("Saved.")
    elif choice == "6":
        save_passwords()
        break
    else:
        print("Invalid choice.")

# This is not really secure.lol.
