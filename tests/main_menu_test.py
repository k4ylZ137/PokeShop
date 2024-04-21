import unittest
from unittest.mock import patch
from main_menu import menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.user = "test_user"
        self.menu = menu(self.user)

    def test_shop_func(self):
        with patch('main_menu.database_manager') as mock_db:
            mock_db.return_value.get_pokemon_listed.return_value = ['Pikachu', 'Charmander']
            with patch('main_menu.store') as mock_store:
                self.menu.shop_func()
                mock_store.assert_called_with(self.user, ['Pikachu', 'Charmander'])

    def test_inventory_func(self):
        with patch('main_menu.database_manager') as mock_db:
            mock_db.return_value.get_pokemon.return_value = ['Bulbasaur', 'Squirtle']
            with patch('main_menu.inventory') as mock_inventory:
                self.menu.inventory_func()
                mock_inventory.assert_called_with(self.user, ['Bulbasaur', 'Squirtle'])

if __name__ == '__main__':
    unittest.main()