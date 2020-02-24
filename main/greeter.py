from time import sleep
import os 

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

### FUNCTIONS ###

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
### PROGRAM ### 

# Set up a loop where users can choose what they'd like to do.
choice = ''
display_title_bar()
while choice != 'q':

    # Response to user choice
    display_title_bar()
    if choice == '1':
        print("\nHere are the people I know.\n")
    elif choice == '2':
        print("\nI can't wait to meet this person!\n")
    elif choice == 'q':
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")


# Lets print a bunch of info in short intervals
names = ['Aaron', 'Brenda', 'Cyrene', 'David', 'eric']

# Prints each name 5 times
for name in names:
    display_title_bar()


    print("\n\n")
    for x in range(0, 5):
        print(name.title())
    
    # Pause for 1 second between cycles
    sleep(1)
