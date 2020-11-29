a,b,c = 1,2,3

print(str(b**c))

# floor division : //

print(str(c//b))

a = [1, 2, 3]
b = [3, 4, 5]
c = [6, 7, 8]

a.extend(b)
print(a)

a.extend(c)
print(a)

a.sort()
print(a)

c = a
d = a.copy()

a.append(9)

print(a)
print(c)
print(d)

a.insert(1200,100)

print(a)