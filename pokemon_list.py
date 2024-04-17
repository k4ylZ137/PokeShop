from inspect_pokemon import *

from models.pokemon import *

import inquirer
from inquirer import List

class pokemon_list:

    def display_pokemon(self, raw_pokemon, current_user):

        pokemon_to_inspect = []
        for pokemon_item in raw_pokemon:
            pokemon_to_inspect.append({
                'name': pokemon_item[1], 'id': pokemon_item[0], 'user': pokemon_item[3], 'price': pokemon_item[2], 'listed': pokemon_item[4]
            })

        # Create a list of Pokemon names
        pokemon_names = [p['name'] + " -- " + str(p['price'] + 0.99) + " PokeBts 🪙" for p in pokemon_to_inspect]
        pokemon_names.append('Return to previous page 🔙')

        questions = [
            List('pokemon',
                message="Which Pokemon do you want to take a look at?",
                choices=pokemon_names,
            ),
        ]

        answers = inquirer.prompt(questions)

        if answers == 'Return to previous page 🔙':
            return

        # Find the selected Pokemon object
        selected_pokemon = next(
            (p for p in pokemon_to_inspect
                if p['name'] + " -- " + str(p['price'] + 0.99) +
                " PokeBts 🪙" == answers['pokemon']), None
        )

        if selected_pokemon is None:
            return

        inspect = inspect_pokemon(pokemon(selected_pokemon['name'], selected_pokemon['id'], selected_pokemon['user'], selected_pokemon['listed']), current_user)
        inspect.display()
        return