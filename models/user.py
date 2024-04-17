import bcrypt
import rich
from rich.panel import Panel
import inquirer

class user:

    def __init__(self, username, password, id, decode=False):
        self.id = id
        self.username = username
        if decode:
            self.password = password
        else:
            self.password = self.hash_password(password)
        self.pokebits = 1500

    def get_username(self):
        return self.username

    def get_pokebits(self):
        return self.pokebits

    def hash_password(self, password):
        # Hash the password using bcrypt
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def compare_password(self, password):
        # Compare the password
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
