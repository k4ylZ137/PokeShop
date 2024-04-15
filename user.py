import bcrypt

class user:

    def __init__(self, username, password, id):
        self.id = id
        self.username = username
        self.password = self.hash_password(password)
        self.pokebits = 1500

    def get_username(self):
        return self.username

    def get_pokebits(self):
        return self.pokebits

    def update_pokebits(self, amount):
        self.pokebits = self.pokebits + amount
        if self.pokebits < -1500:
                print("Insufficient funds for this operation. We are seizing your pokemon and deactiving your account.")
                exit()
        return self.pokebits

    def hash_password(self, password):
        # Hash the password using bcrypt
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def compare_password(self, password):
        # Compare the password
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
