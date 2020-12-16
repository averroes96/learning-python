# Raising an exception

number = input("Enter a positive number:\t")

if(type(number) == int):

    if(int(number) >= 0):
        print("Thank you!")
    else:
        raise Exception("I said a positive number !")

else:
    raise ValueError("I said a number !")