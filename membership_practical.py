### Membership practical ###

admins = [
    "averroes",
    "epicurus",
    "avempace",
    "vigner"
]

username = input("Enter your username:\t").strip().lower()

if username in admins:
    print(f"Hello {username} !")
    option = input("Please chose an option (Delete/Update):\t").strip().lower()

    if(option == "delete"):
        admins.remove(username)
        print("User deleted !")
        print(admins)
    elif option == "update":
        new_username = input("Enter your new username:\t").strip().lower()
        admins[admins.index(username)] = new_username
        print("Your username was successfully updated !")
        print(admins)
    else:
        print("Invalid command !")
else:
    print("No such username !")