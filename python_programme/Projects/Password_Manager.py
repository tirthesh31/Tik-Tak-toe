from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("Key.key","wb") as key_file:
        key_file.write(key)
write_key()
'''
def load_key():
    return open('Key.key','rb').read()

Master_pwd = input("What is the master password? \n")
key = load_key() + Master_pwd.encode()
fer = Fernet(key)

def add():
    name = input("Enter your name. \n")
    pwd = input("Enter Password \n")

    with open('Password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('Password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            usrname, passw = data.split("|")
            print("User:",usrname,"\nPassword:",fer.decrypt(passw.encode()).decode())

while True:
    mode = input("Would like to add new password or to view old password?(add/view) or press q to quit! \n").lower()
    if mode == 'q':
        break

    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("Invalid choice:")
        continue