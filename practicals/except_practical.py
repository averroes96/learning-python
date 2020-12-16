the_file = None
nbr_tries = 3

while nbr_tries > 0:

    try:

        print(f"Enter the file you want to open with its abs path (You've got {nbr_tries} try(ies) left)")
        print(r"Example\t D:\files\your_file.ext")

        file_name_and_path = input("File with its full path: ").strip()

        the_file = open(file_name_and_path, "r")

        print(the_file.read())

        break

    except FileNotFoundError:
        print("Make sure the file exists and its absolute path is correct ")
        nbr_tries -= 1

    except:
        print("Uknown error !")

    finally:
        if(the_file != None):
            the_file.close()
            print("File closed.")

else:
    print("Tries over")

