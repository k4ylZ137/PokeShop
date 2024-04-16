from rich.panel import Panel

import requests

def get_pokemon_catch_rate(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        catch_rate = pokemon_data['capture_rate']
        return catch_rate
    else:
        print(f'Error: {response.status_code}')
        return None

def get_pokemon_is_legendary(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        is_legendary = pokemon_data['is_legendary']
        return is_legendary
    else:
        print(f'Error: {response.status_code}')
        return None

def get_pokemon_is_mythical(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        is_mythical = pokemon_data['is_mythical']
        return is_mythical
    else:
        print(f'Error: {response.status_code}')
        return None

def get_pokemon_for_inspect(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/{name}/'.format(name=pokemon)

    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_sprite = pokemon_data['sprites']['other']['official-artwork']['front_default']
        pokemon_stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
        pokemon_types = [type['type']['name'] for type in pokemon_data['types']]
        pokemon_weight = pokemon_data['weight']
        pokemon_height = pokemon_data['height']

        # Get the evolution chain
        species_url = pokemon_data['species']['url']
        species_response = requests.get(species_url)
        if species_response.status_code == 200:
            species_data = species_response.json()
            evolution_chain_url = species_data['evolution_chain']['url']
            evolution_chain_response = requests.get(evolution_chain_url)
            if evolution_chain_response.status_code == 200:
                evolution_chain_data = evolution_chain_response.json()
                pokemon_evolution_chain = [species['species']['name'] for species in evolution_chain_data['chain']['evolves_to']]

        return {
            'sprite': pokemon_sprite,
            'stats': pokemon_stats,
            'types': pokemon_types,
            'weight': pokemon_weight,
            'height': pokemon_height,
            'evolution_chain': pokemon_evolution_chain
        }
    else:
        print(Panel(f'PokeAPI Error: {response.status_code}', style='red'))
        return None

def get_evolution_chain(pokemon_name):
    # Get the Pokemon species data
    species_response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}')
    species_data = species_response.json()
    # Get the ID of the evolution chain
    evolution_chain_url = species_data['evolution_chain']['url']
    evolution_chain_id = evolution_chain_url.split('/')[-2]
    # Get the evolution chain data
    evolution_response = requests.get(f'https://pokeapi.co/api/v2/evolution-chain/{evolution_chain_id}')
    evolution_data = evolution_response.json()

    # Extract the names of the Pokemon in the evolution chain
    def extract_names(evolves_to):
        names = []
        for evolution in evolves_to:
            names.append(evolution['species']['name'])
            names += extract_names(evolution['evolves_to'])
        return names
    base_species = evolution_data['chain']['species']['name']
    evolutions = extract_names(evolution_data['chain']['evolves_to'])
    return [base_species] + evolutions