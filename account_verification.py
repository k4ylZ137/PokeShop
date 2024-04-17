from rich.panel import Panel
from rich.prompt import Prompt

from inputs import *
from models.user import *
from interaction.db_interaction import database_manager

import models.pokemon as pokemon

db = database_manager()

back_message = Panel('Enter "back" to return to the previous menu. 🔙')

def sign_up():

    print(back_message)
    print()

    valid = False
    while valid == False:
        username = Prompt.ask("Enter your username").lower()
        if check_back_out(username):
            return
        valid = not check_username_exists(username)

        if not valid:
            print(Panel("Username already exists, Please try again.", style="bold red"))
            print()

    valid = False
    while valid == False:
        password = Prompt.ask("Enter your Password", password=True).lower()
        if check_back_out(password):
            return
        confirm_password = Prompt.ask("Re-enter your Password", password=True).lower()
        if check_back_out(confirm_password):
            return
        valid = password == confirm_password and bool(re.search(r'\d', password)) and bool(re.search(r'\w', password))

        if not valid:
            print(Panel("Passwords must match and include Letters and Numbers, Please try again.", style="bold red"))
            print()

    #Sets up new user
    new_user = user(username, password, 0)
    db.insert_user(new_user.username, new_user.password)
    #Fetches again so we can get id, for more efficient searches later
    choose_starter_pokemon(new_user)
    print()
    return db.get_user_by_name(username)[0][0]


def sign_in():

    print(back_message)
    print()

    username = None
    valid = False
    attempts = 0

    # Loop to check if the username exists in records
    while not valid:
        username = Prompt.ask("Enter your Username").lower()
        if check_back_out(username):
            return
        valid = check_username_exists(username)

        if not valid:
            print(Panel("Account does not exist, Please try again.", style="bold red"))
            print()

    # Loop to check if the password matches the entered username
    valid = False
    while not valid and attempts < 3:
        password = Prompt.ask("Enter your Password", password=True).lower()
        if check_back_out(password):
            return
        valid = check_password_matches(password, username)

        if not valid:
            print(Panel("Incorrect password, Please try again.", style="bold red"))
            print()
            attempts += 1

        if attempts == 3:
            print(Panel("Too many invalid attempts. Please try again later.", style="bold red"))
            return

    print()
    return db.get_user_by_name(username)[0][0]


def check_username_exists(username):
    users = db.get_users()
    #Loops over all user objects and checks if the username exists
    for user in users:
        if user[1].lower() == username:
            return True

def check_password_matches(password, username):
    #Accesses the user with the username entered
    raw_user = db.get_user_by_name(username)
    user_to_check = user(raw_user[0][1], raw_user[0][2], raw_user[0][0], decode=True)

    return user_to_check.compare_password(password)

def check_back_out(input):
    if input == 'back':
        print(Panel("Returning to the previous menu. 🔙", style="bold"))
        return True

def sign_up_or_in():
    while True:
        print('\n')
        print(Panel("Would you like to 'Sign Up'🔒 or 'Sign In'🔑?, type 'help' for a list of inputs.", padding=(1, 2), style="bold", title="Account Verification 🔐", title_align="left"))
        input_dict = {
            'sign up': ('Create a new account 🔒', sign_up),
            'sign in': ('Sign in to an existing account 🔑', sign_in)
        }

        result = handle_inputs(input_dict)
        if result:
            break
    return result

def choose_starter_pokemon(user):
    print("\n")
    choice = inquirer.list_input(
        message="Choose your starter Pokemon from the following options: Bulbasaur, Charmander, Squirtle 🔥🌿💧:",
        choices=["Bulbasaur 🌿", "Charmander 🔥", "Squirtle 💧"]
    )

    if choice == "Bulbasaur 🌿":
        choice = "bulbasaur"
    elif choice == "Charmander 🔥":
        choice = "charmander"
    else:
        choice = "squirtle"

    id = db.get_user_by_name(user.username)[0][0]

    temp_pokemon = pokemon.pokemon(choice.lower(), 0, id)
    db.insert_pokemon([temp_pokemon])