#from base64 import decode
#from cgitb import text
#unused imports ^
from cryptography.fernet import Fernet


def load_key():
    try:
        file = open("key.key", "rb")
        key = file.read()
    except:
        file = open("key.key", "wb")
        key = Fernet.generate_key()
        file.write(key)
        file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', "r") as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User :", user, "Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open('password.txt ', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("Do u wanna add a new password or view existing ones (view, add), or press 'q' to exit?").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Try again")
        continue
