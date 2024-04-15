import interaction.pokeapi_interaction as pokeapi_interaction

import rich
from rich import print
from rich.panel import Panel
from rich.text import Text

from PIL import Image
import ascii_magic
import tempfile

import requests
from io import BytesIO

import inputs

from main_menu import *

class inspect_pokemon:
    """
    A class representing a Pokemon inspector.

    Attributes:
    - name (str): The name of the Pokemon.
    - sprite (str): The URL of the Pokemon's sprite image.
    - abilities (list): The abilities of the Pokemon.
    - stats (dict): The stats of the Pokemon.
    - types (list): The types of the Pokemon.
    - weight (int): The weight of the Pokemon.
    - height (int): The height of the Pokemon.
    - evolution_chain (list): The evolution chain of the Pokemon.
    """

    def __init__(self, inspect_pokemon, current_user):

        """
        Initializes a new instance of the inspect_pokemon class.
        To use, call within the Store or Inventory class and instantiate it with your pokemon

        Parameters:
        - inspect_pokemon (str): The name of the Pokemon to inspect.
        """

        poke_api = pokeapi_interaction
        self.current_user = current_user
        self.pokemon = inspect_pokemon
        self.name = inspect_pokemon.name
        self.price = inspect_pokemon.price

        pokemon_data = poke_api.get_pokemon_for_inspect(self.name)
        self.sprite = pokemon_data['sprite']
        self.stats = pokemon_data['stats']
        self.types = pokemon_data['types']
        self.weight = pokemon_data['weight']
        self.height = pokemon_data['height']
        self.evolution_chain = poke_api.get_evolution_chain(self.name)

    def display(self):

        """
        Displays the information of the inspected Pokemon.
        """

        print("\n"*2)
        title = Text("Inspecting " + self.name + " -- " + str(self.price) + " PokeBts 🪙", justify="center")
        print(Panel(title, style='bold', title='INSPECT', padding=(1, 1)))

        self.print_sprite(self.sprite)

        info_text = (
            f"\tStats: {', '.join(f'{k}: {v}' for k, v in self.stats.items())}\n"
            f"\tTypes: {', '.join(self.types)}\n"
            f"\tWeight: {self.weight}\n"
            f"\tHeight: {self.height}"
        )

        print(Panel(Text(info_text), title='STATS', style='bold', padding=(1, 1)))

        print(Panel(Text('    >    '.join(self.evolution_chain), justify='center'), title='EVOLUTION CHAIN', style='bold blue', padding=(1, 1)))

        print("\n")

        # Define input dictionary
        input_dict = {
            'return': ('Back out to previous page', render_main_menu),
        }

        title = 'What would you like to do?'
        text = '  Would you like to '

        if self.pokemon.listed:
            input_dict['rmlist'] = ('Remove listing', self.list_pokemon)
            text += 'Remove listing (rmLists), '
        else:
            input_dict['list'] = ('List Pokemon for sale', self.list_pokemon)
            text += 'List this Pokemon (Pokemon), '

        if self.current_user != self.pokemon.user:
            input_dict['buy'] = ('Buy this pokemon', self.buy)
            text += 'Buy, '

        text += 'or Return?'

        rich.print(Panel(text, title=title))
        inputs.handle_inputs(input_dict)

    def buy(self):
        print('buying...')
        self.pokemon.sell('ash')

    def list_pokemon(self):
        print('listing...')
        self.pokemon.set_listed()

    def print_sprite(self, sprite):

        """
        Prints the sprite image of the Pokemon.

        Parameters:
        - sprite (str): The URL of the Pokemon's sprite image.
        """

        # Download the image
        response = requests.get(sprite)
        image = Image.open(BytesIO(response.content))

        # Resize the image
        max_size = (80, 80)  # Change these numbers to adjust the size
        image.thumbnail(max_size)
        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
            image.save(temp.name)
        # Convert the sprite to ASCII with the specified options
        output = ascii_magic.from_image(temp.name)
        output.to_terminal()
