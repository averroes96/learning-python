# file.write(str) : write and override the current content of a file

file = open(r"test.txt", "w")
file.write("Languages:\n")

# file.writelines(iterable) : write in the file the elements of the iterable object

elments = [ "Java\n", "PHP\n", "C\n"]
file = open(r"test.txt", "w")
file.writelines(elments)

# append
file = open(r"test.txt", "a")
file.write("Python")