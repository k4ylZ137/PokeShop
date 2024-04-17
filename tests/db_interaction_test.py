import unittest

from interaction.db_interaction import database_manager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db = database_manager(':memory:')

    def tearDown(self):
        self.db.close_connection()

    def test_insert_user(self):
        self.db.insert_user('user1', 'password1')
        self.db.insert_user('user2', 'password2')
        users = self.db.get_users()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0][1], 'user1')
        self.assertEqual(users[1][1], 'user2')

    def test_get_user_by_name(self):
        self.db.insert_user('user1', 'password1')
        self.db.insert_user('user2', 'password2')
        user = self.db.get_user_by_name('user1')
        self.assertEqual(len(user), 1)
        self.assertEqual(user[0][1], 'user1')

    def test_insert_pokemon(self):
        class Pokemon:
            def __init__(self, name, price, listed, user):
                self.name = name
                self.price = price
                self.listed = listed
                self.user = user

        pokemon_list = [
            Pokemon('Pikachu', 100, True, 1),
            Pokemon('Charizard', 200, False, 2),
            Pokemon('Bulbasaur', 50, True, 1)
        ]
        self.db.insert_pokemon(pokemon_list)
        pokemon = self.db.get_pokemon(1)
        self.assertEqual(len(pokemon), 2)
        self.assertEqual(pokemon[0][1], 'Pikachu')
        self.assertEqual(pokemon[1][1], 'Bulbasaur')

    def test_get_pokemon_listed(self):
        class Pokemon:
            def __init__(self, name, price, listed, user):
                self.name = name
                self.price = price
                self.listed = listed
                self.user = user

        pokemon_list = [
            Pokemon('Pikachu', 100, True, 1),
            Pokemon('Charizard', 200, False, 2),
            Pokemon('Bulbasaur', 50, True, 1)
        ]
        self.db.insert_pokemon(pokemon_list)
        listed_pokemon = self.db.get_pokemon_listed()
        self.assertEqual(len(listed_pokemon), 2)
        self.assertEqual(listed_pokemon[0][1], 'Pikachu')
        self.assertEqual(listed_pokemon[1][1], 'Bulbasaur')

if __name__ == '__main__':
    unittest.main()