import bcrypt

class user:
    _all_users = []

    def __init__(self, username, password, inventory=[]):
        self.username = username
        self.password = self.hash_password(password)
        self.inventory = inventory
        self.pokebits = 1500

        self._all_users.append(self)

    def get_username(self):
        return self.username

    def get_inventory(self):
        return self.inventory

    def get_pokebits(self):
        return self.pokebits

    def update_pokebits(self, amount):
        self.pokebits = self.pokebits + amount
        if self.pokebits < -1500:
                print("Insufficient funds for this operation. We are seizing your pokemon and deactiving your account.")
        return self.pokebits

    def set_current_user(self, user):
         self.current_user = user

    def get_current_user(self):
         return self.current_user

    def hash_password(self, password):
        # Hash the password using bcrypt
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def compare_password(self, password):
        # Compare the password
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
