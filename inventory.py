from rich import print
from rich.panel import Panel
from rich.text import Text

from interaction.db_interaction import database_manager

from pokemon_list import pokemon_list


class inventory(pokemon_list):

    def __init__(self, current_user, listed_pokemon):

        db = database_manager()
        user = db.get_user(current_user)

        text = ("What Pokemon would you like to take a look at?\n"
        + str(user[0][1]) + ", Your Pokebits " + str(user[0][3]) + " PokeBts 🪙")

        title = Text(text, justify="center")
        print(Panel(title, style='bold', title='Inventory', padding=(1, 1)))
        print()

        if len(listed_pokemon) < 1:
            print(Panel('Oh no you have no Pokemon!'))
            return

        super().display_pokemon(listed_pokemon, current_user)
