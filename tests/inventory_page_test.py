import unittest
from unittest.mock import Mock, patch#
from io import StringIO
from inventory import inventory

class TestInventory(unittest.TestCase):

    @patch('inventory.database_manager')
    @patch('sys.stdout', new_callable=StringIO)

    def test_init_with_no_pokemon(self, mock_stdout, mock_db_manager):
        mock_db_manager.return_value.get_user.return_value = [('username','Johnny', 'Black', 100)]
        inventory('username', [])
        self.assertIn( 'What Pokemon would you like to take a look at?', mock_stdout.getvalue())
        self.assertIn('Johnny, Your Pokebits 100 PokeBts 🪙', mock_stdout.getvalue())
        self.assertIn('Oh no you have no Pokemon!', mock_stdout.getvalue())

if __name__ == '__main__':
            unittest.main()