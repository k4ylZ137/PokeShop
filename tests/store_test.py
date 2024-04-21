import unittest
from unittest.mock import patch
from io import StringIO
from store import store 

class TestStore(unittest.TestCase):
    
    @patch('store.database_manager')
    @patch('sys.stdout', new_callable=StringIO)
    
    def test_init_with_no_pokemon(self, mock_stdout, mock_db_manager):
        mock_db_manager.return_value.get_user.return_value = [('username','Johnny', 'Black', 100)]
        store - store('username', [])
        expected_output - "Oh there is no Pokemon to display!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_init_with_pokemon(self, mock_stdout, mock_db_manager):
        mock_db_manager.return_value.get_user.return_value = [('username', 'John', 'Doe', 100)]
        pokemon_data = [{'name': 'Pikachu', 'price': 50}, {'name': 'Charmander', 'price': 30}]
        store_instance = store('username', pokemon_data)
        expected_output = "What would you like to buy today?\nJohn, Your Pokebits 100 PokeBts 🪙\n"
        self.assertIn(expected_output, mock_stdout.getvalue())
        
        if __name__ == '__main__':
            unittest.main()