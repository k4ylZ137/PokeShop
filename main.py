from inputs import *
from user import *
from account_verification import *

def main():
    print("\n" + "-"*60)
    print("\nWould you like to Sign-up or Sign-in? (sign-up/sign-in)\n")
    print("-"*60)

    #Gets the user to pick if they want to sign in or sign up
    input_dict = ({
            'sign-up': ('Allows you to create a new account', sign_up),
            'sign-in': ('Allows you to log into your account', sign_in),
        })

    handle_inputs(input_dict)

main()