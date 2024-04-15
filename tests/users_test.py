import unittest
from user import user

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = user("testuser", "password123", 1)

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), "testuser")

    def test_get_pokebits(self):
        self.assertEqual(self.user.get_pokebits(), 1500)

    def test_update_pokebits(self):
        self.assertEqual(self.user.update_pokebits(500), 2000)
        self.assertEqual(self.user.update_pokebits(-1000), 1000)
        self.assertEqual(self.user.update_pokebits(-2500), -1500)

    def test_hash_password(self):
        hashed_password = self.user.hash_password("password123")
        self.assertTrue(self.user.compare_password("password123"))
        self.assertFalse(self.user.compare_password("wrongpassword"))

if __name__ == '__main__':
    unittest.main()