# try... except

try:
    number = int(input("Enter your age:\t"))

except ValueError:
    print("Your age dumbass !")

else:
    print(f"Your age is : {number} years old" )

finally: # Execute code no matter what happened
    print("=" * 48)
