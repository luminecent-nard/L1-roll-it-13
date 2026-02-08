
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

#main routine

want_instructions = yes_no("do you want the instructions: ")

print("finished :)")


