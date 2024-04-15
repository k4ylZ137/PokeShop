import inputs
import rich
from rich.panel import Panel

def render_main_menu():
	"""
	Render the main menu.
	"""
	print()
	title = 'Welcome to the Pokemon Market!'
	text = '\tWould you like to Search, Shop or look at your Inventory? (search/shop/inventory)'
	rich.print(Panel(text, title=title, padding=(1,1)))

	# Define input dictionary
	input_dict = {
		'shop': ('Search the platform for listed pokemon to buy', shop_func),
		'inventory': ('Look at your inventory and list pokemon', inventory_func)
	}

	inputs.handle_inputs(input_dict)

def shop_func():
    print('shopping...')

def inventory_func():
    print('inventory...')