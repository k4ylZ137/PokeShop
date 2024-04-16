import random
from models.user import user
import requests

import interaction.db_interaction as db
import models.pokemon as pokemon

# Get a cheeky import script

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1000')
all_pokemon_data = response.json()

all_pokemon_names = [pokemon['name'] for pokemon in all_pokemon_data['results']]
random_pokemon_names = random.sample(all_pokemon_names, 10)

# Create a user
new_user = user("Admin", "$2y$10$.ugXFUFA3yzBKhE5jrCFKuRSZhQiEsOXkBtHruvOA0Ow/T2ZP2WmC", "admin@example.com", 1)
db.database_manager().insert_user(new_user.username, new_user.password)

pokemon_list = []

for index, rand_pokemon in enumerate(random_pokemon_names):
	pokemon_list.append(pokemon.pokemon(rand_pokemon, index, new_user.id))

db.database_manager().insert_pokemon(pokemon_list)


