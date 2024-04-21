import unittest
from unittest.mock import patch
from io import StringIO
from store import store 

class TestStore(unittest.TestCase):
    
    @patch('store.database_manager')
    @patch('sys.stdout', new_callable=StringIO)
    
    def test_init_with_no_pokemon(self, mock_stdout, mock_db_manager):
        mock_db_manager.return_value.get_user.return_value = [('username','Johnny', 'Black', 100)]
        store('username', [])
        self.assertIn( 'Johnny, Your Pokebits 100 PokeBts 🪙', mock_stdout.getvalue())
        self.assertIn('What would you like to buy today?', mock_stdout.getvalue())
        self.assertIn('Oh there is no Pokemon to display!', mock_stdout.getvalue())
        
if __name__ == '__main__':
    unittest.main()