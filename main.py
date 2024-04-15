from inputs import *
from models.user import *
from account_verification import *
from main_menu import *

def main():
	account = sign_up_or_in()
	render_main_menu()
main()