from account_verification import account_verification
from main_menu import menu

def main():
    # account = sign_up_or_in()
    sign_in = account_verification()
    current_user = sign_in.get_response()
    main = menu(current_user)
    main.render_main_menu()

main()