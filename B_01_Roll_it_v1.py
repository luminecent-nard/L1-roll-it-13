
#functions

def yes_no(question):
    """checks user response to a question that is yes / no (y/n), returns 'yes' or 'no' """

    while True:
        #yes or no
        response = input(question).lower()
        #identify yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("nuh uh")

def instructions():
    """prints instructions"""

    print("""
*** Instructions ***

Roll the dice and !!LETS GO GAMBLING!!   
    """)

def integer_checker():
    """checks that the integer is more than 13"""

    error = "Please enter an integer more that / equal to 13."
    while True:
        try:
            response = int(input("what is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

#main routine

want_instructions = yes_no("do you want the instructions: ")

#display instructions if the user wants to see
if want_instructions == "yes":
    instructions()

game_goal = integer_checker()
print(game_goal)





