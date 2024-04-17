import random
import interaction.pokeapi_interaction as pokeapi_interaction
from interaction.db_interaction import database_manager

db = database_manager()

class pokemon:

    def __init__(self, name, id, user, listed=False):
        self.id = id
        self.name = name
        self.price = self.set_price(name)
        self.listed = listed
        self.user = user

    def set_price(self, name):
        base_price = random.randint(850, 1000)
        price = int(( 1 - ( pokeapi_interaction.get_pokemon_catch_rate(name) / 255 )) * base_price)

        if pokeapi_interaction.get_pokemon_is_legendary(name):
            price *=10
        if pokeapi_interaction.get_pokemon_is_mythical(name):
            price *=7

        return price

    def set_listed(self):
        self.listed = not self.listed
        db.set_pokemon_as_listed(self.id)

    def sell(self, new_user):
        self.listed = False
        self.user = new_user
        db.set_pokemon_as_sold(self.id, new_user.id)

    def __str__(self) -> str:
        return f"{self.name} - {self.price} PokeBts 🪙"
