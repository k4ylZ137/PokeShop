import unittest
from unittest.mock import patch
from interaction.db_interaction import database_manager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db = database_manager(':memory:')  # Use an in-memory database for testing

    @patch('interaction.db_interaction.database_manager')
    def test_insert_user(self, mock_db):
        mock_db.insert_user.return_value = None
        mock_db.get_users.return_value = [(1, 'test_user', 'password', 1500)]
        self.db.insert_user('test_user', 'password')
        users = self.db.get_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], 'test_user')
        self.assertEqual(users[0][2], 'password')
        self.assertEqual(users[0][3], 1500)

    @patch('interaction.db_interaction.database_manager')
    def test_insert_pokemon(self, mock_db):
        class Pokemon:
            def __init__(self, name, price, user, listed):
                self.name = name
                self.price = price
                self.user = user
                self.listed = listed
        pokemon_list = [
            Pokemon('Pikachu', 10.0, 1, False),
            Pokemon('Charizard', 20.0, 1, False),
            Pokemon('Bulbasaur', 5.0, 2, False)
        ]
        mock_db.insert_user.return_value = None
        mock_db.insert_pokemon.return_value = None
        mock_db.get_pokemon.return_value = [
            (1, 'Pikachu', 10.0, 1, False),
            (2, 'Bulbasaur', 5.0, 2, False)
        ]
        self.db.insert_user('user1', 'password1')
        self.db.insert_user('user2', 'password2')
        self.db.insert_pokemon(pokemon_list)
        user1_pokemon = self.db.get_pokemon(1)
        user2_pokemon = self.db.get_pokemon(2)
        self.assertEqual(len(user1_pokemon), 2)
        self.assertEqual(len(user2_pokemon), 1)
        self.assertEqual(user1_pokemon[0][1], 'Pikachu')
        self.assertEqual(user1_pokemon[0][2], 10.0)
        self.assertEqual(user1_pokemon[0][3], 1)
        self.assertEqual(user1_pokemon[0][4], False)
        self.assertEqual(user2_pokemon[0][1], 'Bulbasaur')
        self.assertEqual(user2_pokemon[0][2], 5.0)
        self.assertEqual(user2_pokemon[0][3], 2)
        self.assertEqual(user2_pokemon[0][4], False)

    @patch('interaction.db_interaction.database_manager')
    def test_drop_user(self, mock_db):
        mock_db.insert_user.return_value = None
        mock_db.get_users.return_value = [(1, 'test_user', 'password', 1500)]
        self.db.insert_user('test_user', 'password')
        users = self.db.get_users()
        self.assertEqual(len(users), 1)
        user_id = users[0][0]
        mock_db.drop_user.return_value = None
        self.db.drop_user(user_id)
        users = self.db.get_users()
        self.assertEqual(len(users), 0)

    @patch('interaction.db_interaction.database_manager')
    def test_update_user_pokebts(self, mock_db):
        mock_db.insert_user.return_value = None
        mock_db.get_users.return_value = [(1, 'test_user', 'password', 1500)]
        self.db.insert_user('test_user', 'password')
        users = self.db.get_users()
        self.assertEqual(users[0][3], 1500)
        mock_db.update_user_pokebts.return_value = None
        self.db.update_user_pokebts(users[0][0], 2000)
        users = self.db.get_users()
        self.assertEqual(users[0][3], 2000)

if __name__ == '__main__':
    unittest.main()