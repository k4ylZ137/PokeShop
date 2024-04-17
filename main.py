from account_verification import sign_up_or_in
from main_menu import menu

def main():
    # account = sign_up_or_in()
    current_user = sign_up_or_in()
    main = menu(current_user)
    main.render_main_menu()

main()