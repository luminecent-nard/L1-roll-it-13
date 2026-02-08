
while True:
    #yes or no
    yesno = input("yes or no: ").lower()
    #identify yes or no
    if yesno == "yes" or yesno == "y":
        print("yes")
        break
    elif yesno == "no" or yesno == "n":
        print("no")
        break
    else:
        print("nuh uh")
        continue
print("finished :)")


