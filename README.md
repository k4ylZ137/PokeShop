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

more to come...

====Branching Strategy====

When implementing code, create an issue and then branch into your workspace. 
Type the following into the command-line. 
- git pull
- git checkout {name_of_issue}

When merging code, commit and push, and then assign a code reviewer - when review complete, merge code. 

