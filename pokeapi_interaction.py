import requests
import json

def get_poke_data():
    url = f"https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(url)

    if response.status_code == 200:
        pokemen = response.json()
        return (pokemen)
    else:
        print(f'Error: {response.status_code}')

pokemen = get_poke_data()


