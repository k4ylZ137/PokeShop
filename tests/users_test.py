import unittest
from models.user import user

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = user("testuser", "password123", 1)

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), "testuser")

    def test_get_pokebits(self):
        self.assertEqual(self.user.get_pokebits(), 1500)

    def test_update_pokebits(self):
        self.user.update_pokebits(500)
        self.assertEqual(self.user.get_pokebits(), 2000)

    def test_compare_password(self):
        self.assertTrue(self.user.compare_password("password123"))

if __name__ == '__main__':
    unittest.main()