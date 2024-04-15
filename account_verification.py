from rich.panel import Panel
from rich.prompt import Prompt

from inputs import *
from user import *
from db_interaction import database_manager

db = database_manager()

def sign_up():

    print(Panel('Enter "back" to return to the previous menu.', style="green"))
    print()

    valid = False
    while valid == False:
        username = Prompt.ask("Enter your username").lower()
        check_back_out(username)
        valid = not check_username_exists(username)

        if not valid:
            print(Panel("Username already exists, Please try again.", style="bold red"))
            print()

    valid = False
    while valid == False:
        password = Prompt.ask("Enter your Password", password=True).lower()
        check_back_out(password)
        confirm_password = Prompt.ask("Re-enter your Password", password=True).lower()
        check_back_out(confirm_password)
        valid = password == confirm_password and bool(re.search(r'\d', password)) and bool(re.search(r'\w', password))

        if not valid:
            print(Panel("Passwords must match and include Letters and Numbers, Please try again.", style="bold red"))
            print()

    #Sets up new user
    db.insert_user(username, password)
    #Fetches again so we can get id, for more efficient searches later
    new_user = db.get_user_by_name(username)

    print()

    return user(new_user[0][1], new_user[0][2], new_user[0][0])


def sign_in():

    print(Panel('Enter "back" to return to the previous menu.', style="green"))
    print()

    username = None

    valid = False
    #Loop to check if the username exists in records
    while valid == False:
        username = Prompt.ask("Enter your Username").lower()
        check_back_out(username)
        valid = check_username_exists(username)

        if not valid:
            print(Panel("Account does not exist, Please try again.", style="bold red"))
            print()

    #Loop to check if the password matches the entered username
    valid = False
    while valid == False:
        password = Prompt.ask("Enter your Password", password=True).lower()
        check_back_out(password)
        valid = check_password_matches(password, username)

        if not valid:
            print(Panel("Incorrect password, Please try again.", style="bold red"))
            print()

    new_user = db.get_user_by_name(username)

    print()

    return user(new_user[0][1], new_user[0][2], new_user[0][0])

def check_username_exists(username):
    users = db.get_users()
    #Loops over all user objects and checks if the username exists
    for user in users:
        if user[1].lower() == username:
            return True
        else:
            return False

def check_password_matches(password, username):
    #Accesses the user with the username entered
    raw_user = db.get_user_by_name(username)
    user_to_check = user(raw_user[0][1], raw_user[0][2], raw_user[0][0])

    return user_to_check.compare_password(password)

def check_back_out(input):
    if input == 'back':
        print(Panel("Returning to the previous menu.", style="bold"))
        sign_up_or_in()

def sign_up_or_in():
    print('\n')
    print(Panel("Would you like to 'Sign Up' or 'Sign In'?, type 'help' for a list of inputs.", padding=(1, 2), style="bold", title="ACCOUNT VERIFICATION", title_align="left"))
    input_dict = {
        'sign up': ('Create a new account', sign_up),
        'sign in': ('Sign in to an existing account', sign_in)
    }

    handle_inputs(input_dict)
