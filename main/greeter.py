from time import sleep
import os 

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

# Display a title bar.
print("\t**********************************************")
print("\t***  Greeter - Hello old and new friends!  ***")
print("\t**********************************************")

# Lets print a bunch of info in short intervals
names = ['Aaron', 'Brenda', 'Cyrene', 'David', 'eric']

# Prints each name 5 times
for name in names:
    # Pause for one second between cycles and then add two lines to the CLI
    os.system('cls')

    # Display a title bar.
    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")

    sleep(1)
    print("\n\n")

    for x in range(0, 5):
        print(name.title())
    
    # Pause for 1 second between cycles
    sleep(1)
