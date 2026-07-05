import os
import json
from getpass import getpass
from cryptography.fernet import Fernet
import base64
import hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
PASSWORD_FILE = "passwords.enc"
SALT_FILE = "salt.bin"
def load_salt():
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as file:
            return file.read()
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as file:
        file.write(salt)
    return salt
def derive_key(master_password):
    salt = load_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )
    return key
def save_passwords():
    data = json.dumps(passwords)
    encrypted = fernet.encrypt(data.encode())
    with open(PASSWORD_FILE, "wb") as file:
        file.write(encrypted)
def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return []
    with open(PASSWORD_FILE, "rb") as file:
        encrypted = file.read()
    try:
        decrypted = fernet.decrypt(encrypted)
    except:
        print("Wrong master password!")
        exit()
    return json.loads(decrypted.decode())
master_password = getpass("Enter master password: ")
key = derive_key(master_password)
fernet = Fernet(key)
passwords = load_passwords()
while True:
    print("===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Delete Password")
    print("4. Search Password")
    print("5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        website = input("Website: ")
        username = input("Username: ")
        password = getpass("Password: ")
        entry = {
            "website": website,
            "username": username,
            "password": password
        }
        passwords.append(entry)
        save_passwords()
        print("Password added successfully!")

    elif choice == "2":
        if len(passwords) == 0:
            print("No passwords saved.")
        else:
            for entry in passwords:
                print("------------------------")
                print("Website :", entry["website"])
                print("Username:", entry["username"])
                print("Password:", entry["password"])

    elif choice == "3":
        website = input("Enter website to delete: ")
        found = False
        for entry in passwords:
            if entry["website"].lower() == website.lower():
                passwords.remove(entry)
                save_passwords()
                print("Password deleted.")
                found = True
                break
        if not found:
            print("Website not found.")

    elif choice == "4":
        website = input("Search website: ")
        found = False
        for entry in passwords:
            if website.lower() in entry["website"].lower():
                print("----------------")
                print("Website :", entry["website"])
                print("Username:", entry["username"])
                print("Password:", entry["password"])
                found = True
        if not found:
            print("No matching website.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")