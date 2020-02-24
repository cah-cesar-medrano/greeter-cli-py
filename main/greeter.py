# from time import sleep
import os

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

# FUNCTIONS ###


def display_title_bar():
    # Clears cli between cycles and displays title bar
    os.system('cls')
    # Display a title bar.
    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")


def get_user_choice():
    # let users know what they can do.
    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.\n")

    return input("What would you like to do?")
# PROGRAM ###


# Set up a loop where users can choose what they'd like to do.
names = []

choice = ''
display_title_bar()
while choice != 'q':

    coice = get_user_choice()

    # Response to user choice
    display_title_bar()
    if choice == '1':
        print("\nHere are the people I know.\n")
        for name in names:
            print(name.title())
    elif choice == '2':
        new_name = input("\nPlease tell me this person's name: ")
        names.append(new_name)
        print("\nI'm so happy to know %s!\n" % new_name.title())
    elif choice == 'q':
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")
