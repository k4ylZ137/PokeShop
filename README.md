====Initialise platform=====
To install dependencies just run
pip install -r requirements.txt

====Abstract=====
Showcasing Pokemon from across all regions and generations, PokeShop allows users to buy, sell and discover
Pokemon, leveling-up their poke-experience. 

====Mock-Up====

Log-in systems
===========================================================================
 
	LOGIN or SIGN-UP (signup)
	------------------------------------------------------------------
	Enter your username?
	{User Input}
	Enter your password?
	{User Input}
	------------------------------------------------------------------
	{If pass else loop and notify}
 
===========================================================================
 
 
Log-up systems
===========================================================================
	SIGN-UP or LOGIN (signup)
	------------------------------------------------------------------
	Enter your username?
	{User Input}
	Enter your password?
	{User Input}
	------------------------------------------------------------------
	{If pass else loop and notify}
 
===========================================================================
 
 
Log-in systems
===========================================================================
 
	LOGIN
	------------------------------------------------------------------
	Enter your username?
	{User Input}
	Enter your password?
	{User Input}
	------------------------------------------------------------------
	{If pass else loop and notify}
 
===========================================================================
 
 
Inventory
============================================================================
 
 
	INVENTORY
	------------------------------------------------------------------
	{Player Name}        Money - 100 PokeBts
	------------------------------------------------------------------
	Your Pokemon
 
	{Loops for your pokemon}
	[] {Pokemon name} - {Pokemon Cost}
	[] {Pokemon name} - {Pokemon Cost}
	[] {Pokemon name} - {Pokemon Cost}
	[] {Pokemon name} - {Pokemon Cost}
 
	Do you want to list these pokemon on the store? (Y/n/exit)
 
==============================================================================
 
 
Main Menu
=============================================================================
 
	MAIN MENU
	------------------------------------------------------------------
 
	Would you like to Search, Shop or access Inventory (Search/Shop/Inventory)?
 
	------------------------------------------------------------------
	{User Input}
 
 
=============================================================================
 
 
Search
==============================================================================
 
	SEARCH 🔍
	------------------------------------------------------------------
	{Player Name}        Money - 100 PokeBts
	------------------------------------------------------------------
	{User Input}
	------------------------------------------------------------------
	{loop for Matches}
	[] {Pokemon name} - {Pokemon Cost}
	[] {Pokemon name} - {Pokemon Cost}
	[] {Pokemon name} - {Pokemon Cost}
 
	------------------------------------------------------------------
	Buy pokemon (N/Pokemon Name/exit)?
==============================================================================
 
 
Shop
==============================================================================
 
	SHOP 🔍
	------------------------------------------------------------------
	{Player Name}        Money - 100 PokeBts
	------------------------------------------------------------------
	{User Input}
	------------------------------------------------------------------
	{Loops for first shop items}
	[] {Pokemon name} - {Pokemon Cost}
	[] {Pokemon name} - {Pokemon Cost}
 
	------------------------------------------------------------------
	Buy pokemon (N/Pokemon Name/exit)?
==============================================================================

=====Important Links====

Kanban Board:- https://uofg-thegamblers.atlassian.net/jira/software/projects/POK/boards/2
Pokemon API:- https://pokeapi.co/

====Class Specification====

Refactored Code: 

```
==inventory.py==

class inventory(pokemon_list):

    def __init__(self, current_user, listed_pokemon):

        db = database_manager()
        user = db.get_user(current_user)

        text = ("What Pokemon would you like to take a look at?\n"
        + str(user[0][1]) + ", Your Pokebits " + str(user[0][3]) + " PokeBts 🪙")

        title = Text(text, justify="center")
        print(Panel(title, style='bold', title='Inventory', padding=(1, 1)))
        print()

        if len(listed_pokemon) < 1:
            print(Panel('Oh no you have no Pokemon!'))
            return

        super().display_pokemon(listed_pokemon, current_user)
```
==main_menu.py==
'''
class menu:
    def __init__(self, current_user):
        self.USER = current_user

    def render_main_menu(self):
        while True:
            """
            Render the main menu.
            """
            print()
            title = 'Welcome to the Pokemon Market! 🏪'
            text = '\tWould you like to look at the Store or your Inventory? (shop/inventory)'
            print(Panel(text, title=title, padding=(1,1)))

            # Define input dictionary
            input_dict = {
                'shop': ('Search the platform for listed pokemon to buy', self.shop_func),
                'inventory': ('Look at your inventory and list pokemon', self.inventory_func)
            }

            inputs.handle_inputs(input_dict)

    def shop_func(self):
        db = database_manager()
        listed_pokemon = db.get_pokemon_listed()

        shop_page = store(self.USER, listed_pokemon)

    def inventory_func(self):
        db = database_manager()
        listed_pokemon = db.get_pokemon(self.USER)
	

        inv_page = invenclass TestDatabaseManager(unittest.TestCase):

 ===Testing Stubs and Mocks Examples===

==API Testing==

 '''
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

==Database Testing==

'''
class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db = database_manager(':memory:')  # Use an in-memory database for testing

    @patch('interaction.db_interaction.database_manager')
    def test_insert_user(self, mock_db):
        mock_db.insert_user.return_value = None
        mock_db.get_users.return_value = [(1, 'test_user', 'password', 1500)]
        self.db.insert_user('test_user', 'password')
        users = self.db.get_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], 'test_user')
        self.assertEqual(users[0][2], 'password')
        self.assertEqual(users[0][3], 1500)

    @patch('interaction.db_interaction.database_manager')
    def test_insert_pokemon(self, mock_db):
        class Pokemon:
            def __init__(self, name, price, user, listed):
                self.name = name
                self.price = price
                self.user = user
                self.listed = listed
        pokemon_list = [
            Pokemon('Pikachu', 10.0, 1, False),
            Pokemon('Charizard', 20.0, 1, False),
            Pokemon('Bulbasaur', 5.0, 2, False)
        ]
        mock_db.insert_user.return_value = None
        mock_db.insert_pokemon.return_value = None
        mock_db.get_pokemon.return_value = [
            (1, 'Pikachu', 10.0, 1, False),
            (2, 'Bulbasaur', 5.0, 2, False)
        ]
        self.db.insert_user('user1', 'password1')
        self.db.insert_user('user2', 'password2')
        self.db.insert_pokemon(pokemon_list)
        user1_pokemon = self.db.get_pokemon(1)
        user2_pokemon = self.db.get_pokemon(2)
        self.assertEqual(len(user1_pokemon), 2)
        self.assertEqual(len(user2_pokemon), 1)
        self.assertEqual(user1_pokemon[0][1], 'Pikachu')
        self.assertEqual(user1_pokemon[0][2], 10.0)
        self.assertEqual(user1_pokemon[0][3], 1)
        self.assertEqual(user1_pokemon[0][4], False)
        self.assertEqual(user2_pokemon[0][1], 'Bulbasaur')
        self.assertEqual(user2_pokemon[0][2], 5.0)
        self.assertEqual(user2_pokemon[0][3], 2)
        self.assertEqual(user2_pokemon[0][4], False)

    @patch('interaction.db_interaction.database_manager')
    def test_drop_user(self, mock_db):
        mock_db.insert_user.return_value = None
        mock_db.get_users.return_value = [(1, 'test_user', 'password', 1500)]
        self.db.insert_user('test_user', 'password')
        users = self.db.get_users()
        self.assertEqual(len(users), 1)
        user_id = users[0][0]
        mock_db.drop_user.return_value = None
        self.db.drop_user(user_id)
        users = self.db.get_users()
        self.assertEqual(len(users), 0)

    @patch('interaction.db_interaction.database_manager')
    def test_update_user_pokebts(self, mock_db):
        mock_db.insert_user.return_value = None
        mock_db.get_users.return_value = [(1, 'test_user', 'password', 1500)]
        self.db.insert_user('test_user', 'password')
        users = self.db.get_users()
        self.assertEqual(users[0][3], 1500)
        mock_db.update_user_pokebts.return_value = None
        self.db.update_user_pokebts(users[0][0], 2000)
        users = self.db.get_users()
        self.assertEqual(users[0][3], 2000)

if __name__ == '__main__':
    unittest.main()
'''

====Branching Strategy====

When implementing code, create an issue and then branch into your workspace. 
Type the following into the command-line. 
- git pull
- git checkout {name_of_issue}

When merging code, commit and push, and then assign a code reviewer - when review complete, merge code. 
