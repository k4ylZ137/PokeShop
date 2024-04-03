import sqlite3

class DatabaseManager:
    def __init__(self, db_name='database.db'):
        # Connect to the database (creates a new database if it doesn't exist)
        self.conn = sqlite3.connect(db_name)

        # Create a cursor object to execute SQL queries
        self.cursor = self.conn.cursor()

        # Create a table for users
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                poke_bits NUMBER DEFAULT 1500 NOT NULL
            )
        ''')

        # Create a table for Pokemon
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pokemon (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')

        # Commit the changes
        self.conn.commit()

    def insert_pokemon(self, pokemon_list, user_id):
        for pokemon in pokemon_list:
            self.cursor.execute("INSERT INTO pokemon (name, price, user_id) VALUES (?, ?, ?)", (pokemon['name'], pokemon['price'], user_id))
        self.conn.commit()

    def insert_user(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        return users

    def get_pokemon(self, user_id):
        self.cursor.execute("SELECT * FROM pokemon WHERE user_id = ?", (user_id,))
        pokemon = self.cursor.fetchall()
        return pokemon
