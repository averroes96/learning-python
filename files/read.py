file = open("test.txt", "r")

print(file)

text = file.read() # args: [size] = number of letters to be read, if not specified then all

file = open("test.txt", "r")
limited_text = file.read(5)

print(text)
print("=" * 48)
print(limited_text)

print("=" * 48)

# readline(size) : args: [length] = length of the line to be read

file = open("test.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline(2))

print("=" * 48)

# readlines(size) : args: [size] = length of lines to be read -> returns a list

file = open("test.txt", "r")
print(file.readlines())
file = open("test.txt", "r")
print(file.readlines(16))

print("=" * 48)

# practical

file = open("test.txt", "r")
cpt = 0

for line in file:
    print(f"{cpt+1} => {line}")
    cpt += 1