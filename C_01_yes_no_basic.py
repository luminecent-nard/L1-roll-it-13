#keepgoing stolen from other work
keep_going = ""
while keep_going == "":

    #yes or no
    yesno = input("yes or no: ").lower()
    #identify yes or no
    if yesno == "yes" or yesno == "y":
        print("yes")

    elif yesno == "no" or yesno == "n":
        print("no")

    else:
        print("nuh uh")

    keep_going = input("press any key to exit or enter to go again")

