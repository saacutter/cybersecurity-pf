import sqlite3
from passlib.hash import pbkdf2_sha256 as ph
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64
import random

class PasswordManager:
    def __init__(self):
        self.db = sqlite3.connect("passwords.db")

    def get_db(self):
        return self.db

    def add_password(self, user_id, key):
        # Ask the user for the information to store with this account
        name = ""
        while name == "":
            name = input("What should this account be called? ")
        username = input("Enter the username to be saved: ")
        password = getpass("Enter the password to be saved (leave blank for randomly generated password): ")

        # If the password was blank, randomly generate a password
        if password == "":
            password = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*", k=random.randint(8, 64)))
            accept = input(f"The password for this account will be {password}. Accept (y/n)? ")
            if accept.lower().startswith("y"):
                print("Password accepted!")
            else:
                print("Password rejected. Returning to menu...")
                return

        # Encrypt every field
        username = key.encrypt(username.encode())
        password = key.encrypt(password.encode())

        # Add it to the password table
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO passwords(user_id, name, username, password) VALUES(?, ?, ?, ?)", [user_id, name, username, password])
        self.db.commit()

    def list_all_passwords(self, user_id, key):
        # Retrieve all of the user's passwords
        cursor = self.db.cursor()
        passwords = cursor.execute("SELECT * FROM passwords WHERE user_id = ?", [user_id]).fetchall()

        # Process each account
        accounts = []
        for password in passwords:
            # Attempt to decrypt each field or return an empty string
            name = password[2]
            username = key.decrypt(password[3]).decode() if password[3] != "" else ""
            passkey = key.decrypt(password[4]).decode() if password[4] != "" else ""
            
            # Create the dictionary for the accounts
            account = {
                "name": name,
                "username": username,
                "password": passkey
            }
            accounts.append(account)

        # Sort the list of accounts
        accounts = sorted(accounts, key=lambda account: account["name"].lower())

        # Print each account
        print("\n================Passwords====================")
        for i in range(len(accounts)):
            print(f"{i+1}. {accounts[i]["name"]}")
            print(f"\tUsername: {accounts[i]["username"]}")
            print(f"\tPassword: {accounts[i]["password"]}")
        print("=============================================")

    def get_password(self, user_id, key):
        # Ask the user which account they want to retrieve the password for
        account = input("Enter the desired account name: ")

        # Identify if the user has that as an account name
        cursor = self.db.cursor()
        accounts = cursor.execute("SELECT name, username, password FROM passwords WHERE user_id = ? AND name = ?", [user_id, account]).fetchall()
        if len(accounts) == 0:
            print("No record of an account with that name could be found. Please try again.")
            return
        if len(accounts) > 1:
            print("Multiple records found! Printing details of all of them.")
        
        # Decrypt each field of the result
        for account in accounts:
            name = account[0]
            username = key.decrypt(account[1]).decode() if account[1] != "" else ""
            password = key.decrypt(account[2]).decode() if account[2] != "" else ""

            # Print the account details
            print(f"\n{name}")
            print(f"\tUsername: {username}")
            print(f"\tPassword: {password}")

    def delete_password(self, user_id, key):
        # Ask the user which account they want to retrieve the password for
        account = input("Enter the desired account name: ")

        # Identify if the user has that as an account name
        cursor = self.db.cursor()
        accounts = cursor.execute("SELECT id, name, username, password FROM passwords WHERE user_id = ? AND name = ?", [user_id, account]).fetchall()
        if len(accounts) == 0:
            print("No record of an account with that name could be found. Please try again.")
            return
        if len(accounts) > 1:
            print("Multiple records found!")
        
        # Decrypt each field of the result
        for i in range(len(accounts)):
            name = accounts[i][1]
            username = key.decrypt(accounts[i][2]).decode() if accounts[i][2] != "" else ""
            password = key.decrypt(accounts[i][3]).decode() if accounts[i][3] != "" else ""

            # Print the account details
            print(f"\n{i+1}. {name}")
            print(f"\tUsername: {username}")
            print(f"\tPassword: {password}")
        print()

        # Identify which account needs to be deleted if there are multiple
        if len(accounts) > 1:
            account_id = -1
            while account_id < 1 or account_id > len(accounts):
                account_id = input("Select the ID of the account you want to delete: ")

                try: account_id = int(account_id)
                except ValueError: account_id = -1
        else:
            account_id = 1
        
        # Check with the user that they have selected the correct account
        print("The following account will be deleted:")
        print(f"{accounts[account_id-1][1]}")
        print(f"\tUsername: {key.decrypt(accounts[account_id-1][2]).decode() if accounts[account_id-1][2] != "" else ""}")
        print(f"\tPassword: {key.decrypt(accounts[account_id-1][3]).decode() if accounts[account_id-1][3] != "" else ""}")
        delete = input("Are you sure you want to delete this account (y/n)? ")
        if delete.lower().startswith("y"):
            cursor.execute("DELETE FROM passwords WHERE id = ?", [accounts[account_id-1][0]])
            self.db.commit()
            print("Account deleted.")
        else:
            print("Deletion aborted.")



def main():
    # Create an instance of the password manager
    pw_manager = PasswordManager()
    cursor = pw_manager.get_db().cursor()

    # Let the user login to their account (or create one if it doesn't exist yet)
    username = input("Enter your username: ")
    user = cursor.execute("SELECT * FROM users WHERE username = ?", [username]).fetchone()

    # If the username does not exist ask if the user wants to make an account, otherwise ask for the master password
    if user is None:
        create = input("Do you want to create a new user (y/n)? ")
        if create.lower().startswith("y"):
            # Get the password from stdin
            password = getpass("Choose your password: ")

            # Hash the password
            password = ph.hash(password)

            # Create the salt
            salt = os.urandom(16)

            # Insert the user into the users table
            cursor.execute("INSERT INTO users(username, master_password, salt) VALUES(?, ?, ?)", [username, password, salt])

            print("User successfully created! You have been logged in automatically.")
        else:
            print("No user has been created. Exiting the program...")
            return
    else:
        attempts = 0
        while True:
            # If there have been more than 5 attempts to access an account, stop the program
            attempts += 1
            if attempts >= 6:
                print("Too many password attempts. Please try again later.")
                return
            
            password = getpass(f"Enter password for {username}: ")

            # Get the password for the specified user
            correct_password = cursor.execute("SELECT master_password FROM users WHERE username = ?", [username]).fetchone()[0]

            if ph.verify(password, correct_password):
                print("Logging in...")
                break

    # Commit any changes to the database
    pw_manager.get_db().commit()

    # Create cryptography key using fernet (adapted from https://cryptography.io/en/latest/fernet/)
    user = cursor.execute("SELECT * FROM users WHERE username = ?", [username]).fetchone()
    salt = user[3]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)

    # Let the user select what they want to do
    while True:
        print("\nPlease choose what you want to do.")
        print("1. Add an account.")
        print("2. List all accounts.")
        print("3. Retrieve a singular account.")
        print("4. Delete an account.")
        print("5. Quit.")

        # Retrieve the user's choice
        choice = input("Choice: ")

        if choice == "1":
            pw_manager.add_password(user[0], f)
        elif choice == "2":
            pw_manager.list_all_passwords(user[0], f)
        elif choice == "3":
            pw_manager.get_password(user[0], f)
        elif choice == "4":
            pw_manager.delete_password(user[0], f)
        else:
            break

if __name__ == '__main__':
    main()