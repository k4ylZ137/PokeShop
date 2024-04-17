from rich import print
from rich.panel import Panel
from rich.text import Text

from interaction.db_interaction import database_manager

from pokemon_list import pokemon_list


class inventory(pokemon_list):

    def __init__(self, current_user, listed_pokemon):

        title = Text("What would you like to buy today?", justify="center")
        print(Panel(title, style='bold', title='Store', padding=(1, 1)))
        print()

        if len(listed_pokemon) < 1:
            print(Panel('Oh no you have no Pokemon!'))
            return

        super().display_pokemon(listed_pokemon, current_user)
