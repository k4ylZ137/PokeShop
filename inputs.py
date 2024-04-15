import sys
import re
import inquirer

import rich
from rich import print
from rich.console import Console
from rich.rule import Rule
from rich.panel import Panel


# The idea of this is to use a dictionary subbed into a function to allow us to easily handle input here rather than repeating code 😉
# https://github.com/magmax/python-inquirer

def quit_func():
    print(Rule(style='white'))
    # define a checkbox question, curtosy of Erin
    questions = [
        inquirer.List('confirmQuit',
            message="Are you sure you want to quit",
            choices=['Yes', 'No'],
        ),
    ]
    answers = inquirer.prompt(questions)
    # If selected answer is yes exit program
    if answers['confirmQuit'] == 'Yes':
        sys.exit()
    # Else return to loop
    else:
        return

def help_func(input_dict):
    text = ''
    # Print the attributes in the dictionary in a panel
    for command, (description, _) in input_dict.items():
        text += f"- {command}: {description}"
        if command != list(input_dict.keys())[-1]:
            text += "\n"

    rich.print(Panel(text, title="Available inputs", style="blue"))

def handle_inputs(input_dict: dict):
    # Update the subbed in dict to include static commands
    input_dict.update({
        'quit': ('Quit the program', quit_func),
        'help': ('Display the list of commands and their descriptions', help_func),
    })

    # Loop for commands is help or quit
    while True:
        user_input = input("\nEnter command: ").lower()
        print()
        if user_input == 'help':
            description, func = input_dict[user_input]
            func(input_dict)
        elif user_input in input_dict:
            description, func = input_dict[user_input]
            func()
            break
        else:
            print("Whoops,\nPlease enter one of the following: \n")
            help_func(input_dict)
