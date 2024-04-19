from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from models.pokemon import pokemon
from pokemon_list import pokemon_list
import random
import interaction.pokeapi_interaction as pokeapi_interaction

from interaction.db_interaction import database_manager
db = database_manager()

class search(pokemon_list):

    def __init__(self):
        pass

    def run_page(self, current_user):
        title = Text("What would you like to search for today?", justify="center")
        print(Panel(title, style='bold', title='Search', padding=(1, 1)))
        print()
        pokemon_name = self.get_user_pokemon()

        #checks that user admin does not already have the pokemon assigned to it (if it does it will just return the pokemon that has already been imported from api but update it to listed)
        searched_pokemon = self.get_searched_pokemon(pokemon_name)

        if searched_pokemon == None:
            searched_pokemon = self.insert_pokemon(pokemon_name)

        searched_pokemon = self.update_price(searched_pokemon)
        super().display_pokemon([searched_pokemon], current_user=current_user)

    def get_user_pokemon(self):
        pokemon_name = Prompt.ask("Enter the pokemons name").lower()
        return pokemon_name
    
    def insert_pokemon(self, pokemon_name):
         #setting up a new pokemon object with the name input, the user as admin(id  = 1) and listed as true
        new_pokemon = pokemon(pokemon_name,0,1,True)

        db.insert_pokemon([new_pokemon])
        searched_pokemon = self.get_searched_pokemon(pokemon_name)

        return searched_pokemon

    def get_searched_pokemon(self, pokemon_name):
        searched_pokemon = None
        admin_pokemons = db.get_pokemon(1)
        for admin_pokemon in admin_pokemons:
            if admin_pokemon[1].lower() == pokemon_name.lower():
                searched_pokemon = admin_pokemon
                # changes listed to true
                if searched_pokemon[4] == 0:
                    searched_pokemon = self.update_listed(searched_pokemon)
        return searched_pokemon

    def update_listed(self, searched_pokemon):
        db.set_pokemon_as_listed(searched_pokemon[0])
        list_ = list(searched_pokemon)
        list_[4] = 1
        searched_pokemon = tuple(list_)
        return searched_pokemon


    def update_price(self, searched_pokemon):
        origonal_price = searched_pokemon[2]
        the_10 = origonal_price * 0.1
        new_price = origonal_price + the_10
        db.set_pokemon_price(searched_pokemon[0], new_price)

        list_ = list(searched_pokemon)
        list_[2] = new_price
        searched_pokemon = tuple(list_)
        return searched_pokemon
