import random
import interaction.pokeapi_interaction as pokeapi_interaction
from interaction.db_interaction import database_manager

db = database_manager()

class pokemon:

    def __init__(self, name, id, user):
        self.id = id
        self.name = name
        self.price = self.set_price(name)
        self.listed = False
        self.user = user

    def set_price(self, name):
        price = random.randint(2000, 2300)
        return int(( 1 - ( pokeapi_interaction.get_pokemon_catch_rate(name) / 255 )) * price)

    def set_listed(self):
        self.listed = not self.listed
        db.set_pokemon_as_listed(self.id)

    def sell(self, new_user):
        self.listed = False
        self.user = new_user
        db.set_pokemon_as_sold(self.id, new_user.id)

    def __str__(self) -> str:
        return f"{self.name} - {self.price} PokeBts 🪙"
