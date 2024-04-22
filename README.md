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

        inv_page = inventory(self.USER, listed_pokemon)

 '''
====Branching Strategy====

When implementing code, create an issue and then branch into your workspace. 
Type the following into the command-line. 
- git pull
- git checkout {name_of_issue}

When merging code, commit and push, and then assign a code reviewer - when review complete, merge code. 
