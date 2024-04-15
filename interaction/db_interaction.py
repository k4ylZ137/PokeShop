import sqlite3

class database_manager:
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
                listed BOOLEAN DEFAULT 0,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')

        # Commit the changes
        self.conn.commit()

    def insert_pokemon(self, pokemon_list):
        for pokemon in pokemon_list:
            self.cursor.execute("INSERT INTO pokemon (name, price, user_id) VALUES (?, ?, ?)", (pokemon.name, pokemon.price, pokemon.user))
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

    def get_user_by_name(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        users = self.cursor.fetchall()
        return users

    def get_pokemon(self, user_id):
        self.cursor.execute("SELECT * FROM pokemon WHERE user_id = ?", (user_id,))
        pokemon = self.cursor.fetchall()
        return pokemon

    def set_pokemon_as_listed(self, pokemon_id):
        self.cursor.execute("UPDATE pokemon SET listed = NOT listed WHERE id = ?", (pokemon_id,))
        self.conn.commit()

    def set_pokemon_as_sold(self, pokemon_id, user_id):
        self.cursor.execute("UPDATE pokemon SET user_id = ? WHERE id = ?", (user_id, pokemon_id))
        self.conn.commit()
        self.set_pokemon_as_listed(pokemon_id)