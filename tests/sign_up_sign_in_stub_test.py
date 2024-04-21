import unittest
from unittest.mock import patch
from account_verification import account_verification

class TestSignUpOrIn(unittest.TestCase):
    @patch('account_verification.handle_inputs')
    def test_sign_up_or_in_sign_up(self, mock_handle_inputs):
        mock_handle_inputs.return_value = 'sign up'
        result = account_verification().sign_up_or_in()
        self.assertEqual(result, 'sign up')

    @patch('account_verification.handle_inputs')
    def test_sign_up_or_in_sign_in(self, mock_handle_inputs):
        mock_handle_inputs.return_value = 'sign in'
        result = account_verification().sign_up_or_in()
        self.assertEqual(result, 'sign in')