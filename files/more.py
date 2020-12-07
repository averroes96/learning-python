### file.truncate(size)

#file = open(r"test.txt", "w")
#file.truncate(12)

### file.tell() : returns the index of the last element in the file

#print(file.tell())

### file.seek(offset) : seek the offset you want to start reading the file from

myfile = open(r"test.txt", "r")
myfile.seek(6)
print(myfile.read())

### removing a file

#import os
#os.remove(r"test.txt")