import inputs
from rich import print
from rich.panel import Panel

from interaction.db_interaction import database_manager

from store import store
from inventory import inventory

class menu:
    def __init__(self, current_user):
        self.USER = current_user

    def render_main_menu(self):
        while True:
            """
            Render the main menu.
            """
            print()
            title = 'Welcome to the Pokemon Market! 🏪'
            text = '\tWould you like to look at the Store or your Inventory? (shop/inventory)'
            print(Panel(text, title=title, padding=(1,1)))

            # Define input dictionary
            input_dict = {
                'shop': ('Search the platform for listed pokemon to buy', self.shop_func),
                'inventory': ('Look at your inventory and list pokemon', self.inventory_func)
            }

            inputs.handle_inputs(input_dict)

    def shop_func(self):
        db = database_manager()
        listed_pokemon = db.get_pokemon_listed()

        shop_page = store(self.USER, listed_pokemon)

    def inventory_func(self):
        db = database_manager()
        listed_pokemon = db.get_pokemon(self.USER)

        inv_page = inventory(self.USER, listed_pokemon)

