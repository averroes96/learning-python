# Sets are enclosed in curly brackets
# Sets are neither indexed nor ordered
# No slicing allowed either
# Accepts only immutable data types, dict and list not allowed

mySet = {
    1,
    "Hello",
    2,
    3,
    "four"
}

print(mySet) # run multiple times to see that it's not ordered 

print("=" * 40)

# Items must be unique

secondSet = {
    1,1,1,1,
    2,2,2,
    3,3
}

print(secondSet)

print("=" * 40)

# Methods

### clear()
fruits = {'apple', 'banana', 'cherry'}
fruits.clear()
print(fruits)

print("=" * 40)

### union(set)

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.union(y) 
print(z)

x = {'a', 'b', 'c'}
y = {'f', 'd', 'a'}
z = {'c', 'd', 'e'}
result = x.union(y, z) 
print(result)

print("=" * 40)

### add()

fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange') 
print(fruits)

print("=" * 40)

### copy()

fruits = {'apple', 'banana', 'cherry'}
x = fruits.copy()
x.add("orange")
print(fruits)
print(x)

print("=" * 40)

### discard() // safetly delete an element 

seyfruits = {'apple', 'banana', 'cherry'}
fruits.discard('banana') 
print(fruits)

print("=" * 40)

### pop() // randomly deletes an element

fruits = {'apple', 'banana', 'cherry'}
print(fruits.pop()) 
print(fruits)

print("=" * 40)

### difference(b) => a-b

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = y.difference(x) 
print(z)

print("=" * 40)

### difference_update(b) => update a with the difference between a and b

x.difference_update(y)
print(x)

print("=" * 40)

### intersection(b) => a AND b

x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
z = {'f', 'g', 'c'}
result = x.intersection(y, z)
print(result)

print("=" * 40)

### intersection_update

x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
z = {'f', 'g', 'c'}
x.intersection_update(y)
print(x)

print("=" * 40)

### symmetric_difference(b) elements that doesn't exist in both or all of the sets

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.symmetric_difference(y) 
print(z)

print("=" * 40)

### symmetric_difference_update(b)

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.symmetric_difference_update(y) 
print(x)

print("=" * 40)

### a.issuperset(b) //check if all the elements in b exists in a

x = {'a', 'b', 'c'}
y = {'f', 'e', 'd', 'c', 'b'}
z = x.issubset(y) 
print(z)

print("=" * 40)

### a.issubset(b) //check if all the elements in a exists in b

x = {'a', 'b', 'c'}
y = {'f', 'e', 'd', 'c', 'b', 'a'}
z = x.issubset(y) 
print(z)

print("=" * 40)

### a.isdisjoint(b) //returns true if intersection equals an empty set

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.isdisjoint(y) 
print(z)

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'facebook'}
z = x.isdisjoint(y)
print(z)