from unittest.mock import patch, Mock
import unittest
from interaction.pokeapi_interaction import *

class TestPokeApiController(unittest.TestCase):
    @patch('requests.get')
    def test_get_pokemon_catch_rate(self, mock_get):
        # Arrange
        mock_response = Mock()
        expected_rate = 45
        mock_response.json.return_value = {
            'capture_rate': expected_rate,
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        catch_rate = get_pokemon_catch_rate('bulbasaur')

        # Assert
        self.assertEqual(catch_rate, expected_rate)
    
    @patch('requests.get')
    def test_get_pokemon_is_legendary(self, mock_get):
        # Arrange
        mock_response = Mock()
        expected_rarity = False
        mock_response.json.return_value = {
            'is_legendary': expected_rarity,
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        rarity = get_pokemon_is_legendary('bulbasaur')

        # Assert
        self.assertEqual(rarity, expected_rarity)

    @patch('requests.get')
    def test_get_pokemon_is_mythical(self, mock_get):
        # Arrange
        mock_response = Mock()
        expected_rarity = False
        mock_response.json.return_value = {
            'is_mythical': expected_rarity,
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        rarity = get_pokemon_is_mythical('bulbasaur')

        # Assert
        self.assertEqual(rarity, expected_rarity)

if __name__ == "__main__":
    unittest.main()