import unittest
import sqlite3
import os
from db_interaction import database_manager

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        # Create a new database for testing
        self.db = database_manager('test.db')

    def tearDown(self):
        # Close the connection and remove the test database after each test
        self.db.conn.close()
        os.remove('test.db')

    def test_insert_user(self):
        # Define a test user
        username = 'test_user'
        password = 'test_password'

        # Insert the user into the database
        self.db.insert_user(username, password)

        # Query the database to check if the user was inserted correctly
        self.db.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        data = self.db.cursor.fetchone()

        # Check that the data matches the inserted user
        self.assertEqual(data[1], username)
        self.assertEqual(data[2], password)

    def test_get_users(self):
        # Define a test user
        username = 'test_user'
        password = 'test_password'

        # Insert the user into the database
        self.db.insert_user(username, password)

        # Get the users from the database
        users = self.db.get_users()

        # Check that the returned data matches the inserted user
        self.assertEqual(users[0][1], username)
        self.assertEqual(users[0][2], password)
        self.assertEqual(users[0][3], 1500)

    def test_get_pokemon(self):
        # Define a test user and Pokemon
        username = 'test_user'
        password = 'test_password'
        pokemon_list = [{'name': 'Pikachu', 'price': 100.0}]

        # Insert the user into the database
        self.db.insert_user(username, password)

        # Get the user_id of the inserted user
        self.db.cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        user_id = self.db.cursor.fetchone()[0]

        # Insert the Pokemon into the database
        self.db.insert_pokemon(pokemon_list, user_id)

        # Get the Pokemon from the database
        pokemon = self.db.get_pokemon(user_id)

        # Check that the returned data matches the inserted Pokemon
        self.assertEqual(pokemon[0][1], 'Pikachu')
        self.assertEqual(pokemon[0][2], 100.0)
        self.assertEqual(pokemon[0][3], user_id)

if __name__ == '__main__':
    unittest.main()