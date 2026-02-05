# Functions

def yes_no(question):

    """checks user response to question is yes / no, returns 'yes' or 'no'"""

    while True:

        response = input("Do you want to see the instructions?").lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
           return "no"
        else:
            print("please enter yes or no")


# Main Routine
want_instructions = yes_no("Do you want to see the instructions?")
want_coffee = yes_no("Do you want coffee?")
print("we are done")