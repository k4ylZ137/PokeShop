import unittest
import sqlite3
from unittest.mock import patch

from models.user import user
from models.pokemon import pokemon
from search import search
from interaction.db_interaction import database_manager
db = database_manager()

class TestSearch(unittest.TestCase):

    def setUp(self):
        # Create a admin user and assigns it the following pokemon
        new_user = user("Admin", "$2y$10$.ugXFUFA3yzBKhE5jrCFKuRSZhQiEsOXkBtHruvOA0Ow/T2ZP2WmC", 1, 1)
        db.insert_user(new_user.username, new_user.password)

        pokemon_list = [
            pokemon('eevee', 1, 1),
            pokemon('squirtle', 2, 1),
        ]

        db.insert_pokemon(pokemon_list)

        # Create a customer user
        new_user = user("user", "pass00", 1, 1)
        db.insert_user(new_user.username, new_user.password)

        # Create a cursor object to execute SQL queries
        db.cursor = db.conn.cursor()

    def test_get_user_pokemon(self):
        db.conn.commit()
        search_page = search()

        with patch('builtins.input', return_value='eevee') as _input:
            self.assertEqual('eevee', search_page.get_user_pokemon())

    def test_if_can_detect_admin_pokemon(self):
        search_page = search()

        result = search_page.get_searched_pokemon("eevee")
        self.assertTrue(result[1],"eevee" )

        result = search_page.get_searched_pokemon("squirtle")
        self.assertTrue(result[1],"Squirtle" )


    def test_if_can_detect_not_admin_pokemon(self):
        search_page = search()

        self.assertEqual(search_page.get_searched_pokemon("Pikachu"),None)
        self.assertEqual(search_page.get_searched_pokemon("Mew"),None )


    def test_insert_to_user_if_pokemon_new(self):
        search_page = search()
        admin_pokemons = db.get_pokemon(1)
        for pokemon in admin_pokemons:
            self.assertNotEqual(pokemon[1], "mew")

        searched_pokemon =  search_page.insert_pokemon("mew")

        admin_pokemons = db.get_pokemon(1)
        self.assertEqual(admin_pokemons[len(admin_pokemons)-1][1], "mew")

    def test_update_price(self):
        from models.pokemon import pokemon
        search_page = search()

        db.insert_pokemon([pokemon("pikachu", 5, 2)])
        pokemons = db.get_pokemon(2)

        for pokemon_ in pokemons:
            if pokemon_[1] == "pikachu":
                searched_pokemon = pokemon_
                original_price = pokemon_[2]

        the_10 = original_price * 1.0
        expected_price = original_price + the_10

        result = search_page.update_price(searched_pokemon)
        result = result[2]

        self.assertTrue(result, expected_price)

if __name__ == '__main__':
    unittest.main()