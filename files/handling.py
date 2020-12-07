# File handling

## open(file, mode = r) 
### modes : append(a) , read(r), write(w), create(x)

import os

print("Curr = " + os.getcwd()) # Get current working directory

print(os.path.dirname(os.path.abspath(__file__))) # Get the directory

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Change current working directory

print("Curr = " + os.getcwd())

print(os.path.abspath(__file__)) # Get the absolute path of the current working directory

Zfile = open(r"test.txt")