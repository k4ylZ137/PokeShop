import random
import interaction.pokeapi_interaction as pokeapi_interaction
from interaction.db_interaction import database_manager
from rich.prompt import Confirm
from rich import print

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
        confirm = Confirm.ask("Are you sure you want to List this Pokemon?")
        if confirm:
            self.listed = not self.listed
            db.set_pokemon_as_listed(self.id)

    def sell(self, buyer_id):

        buyer = db.get_user(buyer_id)
        buyer_coin = buyer[0][3]
        new_buyer_coin = buyer_coin - self.price

        if new_buyer_coin <= -1500:
            print("[bold red blink]WARNING: Insufficient funds for this operation. We are seizing your pokemon and deactiving your account. ⚠️![/bold red blink]")
            db.drop_user(buyer[0][0])
            exit()
        else:
            confirm = Confirm.ask("Are you sure you want to Buy this Pokemon?, this would leave you with " + str(new_buyer_coin) + " PokeBts 🪙 S")
            if confirm:
                self.listed = False

                seller = db.get_user(self.user)

                self.user = buyer_id

                db.update_user_pokebts(self.user, new_buyer_coin)
                db.update_user_pokebts(seller[0][0], seller[0][3] + self.price)

                db.set_pokemon_as_sold(self.id, self.user)

            else:
                print("[bold red]Buy Cancelled.[/bold red]")
            return

    def __str__(self) -> str:
        return f"{self.name} - {self.price} PokeBts 🪙"
