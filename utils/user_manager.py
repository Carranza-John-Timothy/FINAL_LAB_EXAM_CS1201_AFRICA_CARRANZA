
class usermanager:
    def __init__(self, username, password):
        user_database = {}
        self.usermanager.username = 'username'
        self.usermanager.password = "password"


def load_users():
    pass
def save_users():
    pass
def validate_username():
    pass
def validate_password():
    pass
def login():
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))

    if username in usermanager.user_database.username and usermanager.user_database[username].password == password:
        print(f"Welcome {username}! ")
    else:
        print("Username or password wrong.")
        return

def register():
    username = str(input("Enter USERNAME: "))
    password = str(input("Enter PASSWORD: "))

    if len(username) <= 4:
        print("Username must be atleast 4 characters long.")
        return
    else:
        for username in usermanager.user_database.username

    if len(password) <= 8:
        print("Password must be 8 characters long.")
        return
    else:
