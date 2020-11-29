# Tuples can be written in 2 ways

# First:
myTuple = (1, 2, 3, 4)

# Second:
myTuple2 = 1,2,3,4

print(myTuple2)

# Tuples indexting

print(myTuple[0])
print(myTuple[-1])

# Tuples are immutable > You can't add or delete or edit them

#myTuple[0] = "one" # Throws an error

# To tell python that your variable is a tuple in case of 1 element add "," after

tpl = 1,

print(type(tpl))

# Concatenation

a,b = (1,2,3),(4,5)

a += ("6", True) + b

print(a)

# Repeating elements

print(a * 3)

# Methods

## count() => count how many times an element is repeated in the tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

## index() => index of a given element

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

# Spreading tuple elements

a = (1,2,3,4)
x, y, _, z = a # _ is used to ignore an element 

print(x)
print(y)
print(z)