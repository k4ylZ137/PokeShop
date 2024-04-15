from inputs import *
from user import *

def sign_up():
    valid = False
    #Loop to check if the username exists in records
    while valid == False:
        username = input("Enter your username: ").lower()
        valid = check_username_unique(username)

    password = input("Enter your password: ")

    #Sets up new user
    valid_user = user(username, password)

    #Sets the current user as the account just created
    valid_user.set_current_user(valid_user)
    print("-"*60)

def sign_in():
    print("\n" + "-"*60 + "\n")

    valid = False

    #Loop to check if the username exists in records
    while valid == False:
        username = input("Enter your username: ").lower()
        valid = check_username_exists(username)

    #Loop to check if the password matches the entered username
    valid = False
    while valid == False:
        password = input("Enter your password: ")
        valid = check_password_matches(password)
    print("-"*60)

def check_username_exists(username):
    #Loops over all user objects
    for user in user._all_users:
        if user.get_username().lower() == username:

            #Sets the current user as the user with the username entered
            user.set_current_user(user)
            return True
        else:
            print("Username does not exist. Try again.")
            return False

def check_password_matches(password):
    #Accesses the user with the username entered
    current_user = user._all_users[0].get_current_user()

    if user.compare_password(current_user, password) == True:
        return True
    else:
        print("Password does not match. Try again.")
        return False

def check_username_unique(username):
    #Sets up a list of all usernames
    taken_names = []

    for user in user._all_users:
        taken_names.append(user.get_username().lower())

    #Checks if username already in use or not
    if username in taken_names:
        print("Username already taken. Try again.")
        return False
    else:
        return True
