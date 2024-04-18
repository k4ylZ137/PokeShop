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
        self.listed = inspect_pokemon.listed

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
        print(Panel(title, style='bold', title='Inspect', padding=(1, 1)))

        self.print_sprite(self.sprite)

        info_text = (
            f"\tStats: {', '.join(f'{k}: {v}' for k, v in self.stats.items())}\n"
            f"\tTypes: {', '.join(self.types)}\n"
            f"\tWeight: {self.weight}\n"
            f"\tHeight: {self.height}"
        )

        print(Panel(Text(info_text), title='Stats', style='bold', padding=(1, 1)))

        print(Panel(Text('    >    '.join(self.evolution_chain), justify='center'), title='Evolution Chain', style='bold blue', padding=(1, 1)))

        print("\n")

        # Define input dictionary
        input_dict = {
            'rtn': ('Return to previous page', self.back_out),
        }

        title = 'What would you like to do?'
        text = '  Would you like to '

        if self.current_user == self.pokemon.user:
            if self.pokemon.listed:
                input_dict['unlist'] = ('Remove listing', self.unlist_pokemon)
                text += 'Remove listing (unlist), '
            else:
                input_dict['list'] = ('List Pokemon for sale', self.list_pokemon)
                text += 'List this Pokemon (list), '

        if self.current_user != self.pokemon.user and self.pokemon.listed:
            input_dict['buy'] = ('Buy this pokemon', self.buy)
            text += 'Buy this Pokemon (buy), '

        text += 'or Return (rtn)?'

        rich.print(Panel(text, title=title))
        inputs.handle_inputs(input_dict)

    def buy(self):
        print(Panel('Buying Pokemon...'))
        self.pokemon.sell(self.current_user)

    def list_pokemon(self):
        print(Panel('listing Pokemon...'))
        self.pokemon.set_listed()

    def unlist_pokemon(self):
        print(Panel('unlisting Pokemon...'))
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

    def back_out(self):
        return