import unittest

import sys
sys.path.append('../')

from user import user

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = user('test_user', 'test_password')

    def test_get_username(self):
        # Check that the username is correct
        self.assertEqual(self.user.get_username(), 'test_user')

    def test_get_inventory(self):
        # Check that the inventory is empty
        self.assertEqual(self.user.get_inventory(), [])

    def test_get_pokebits(self):
        # Check that the pokebits is 1500
        self.assertEqual(self.user.get_pokebits(), 1500)

    def test_update_pokebits(self):
        # Update the user's pokebits
        self.user.update_pokebits(500)

        # Check that the user's pokebits were updated correctly
        self.assertEqual(self.user.get_pokebits(), 2000)#

    def test_compare_password(self):
        self.user = user('test_user', 'test_password')
        self.assertTrue(self.user.compare_password('test_password'))
        self.assertFalse(self.user.compare_password('wrong_password'))

if __name__ == '__main__':
    unittest.main()