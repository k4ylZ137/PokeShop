import inputs
import rich
from rich.panel import Panel

# Print formatting for the main menu
print()
title = 'Welcome to the Pokemon Market!'
text = '   Would you like to Search, Shop or look at your Inventory? (search/shop/inventory)'
rich.print(Panel(text, title=title, padding=(1,1)))

# Placeholder functions
def search_func():
    print('searching...')

def shop_func():
    print('shopping...')

def inventory_func():
    print('inventory...')

# Define input dictionary
input_dict = {
    'search': ('Search the platform for new pokemon to buy', search_func),
    'shop': ('Search the platform for listed pokemon to buy', shop_func),
    'inventory': ('Look at your inventory and list pokemon', inventory_func)
}

inputs.handle_inputs(input_dict)