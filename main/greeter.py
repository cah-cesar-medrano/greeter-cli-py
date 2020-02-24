from time import sleep
import os 

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.


def display_title_bar():
    # Clears cli between cycles and displays title bar
    os.system('cls')
    # Display a title bar.
    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")

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
