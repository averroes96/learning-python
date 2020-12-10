## all(iterable): returns true if all the elements of the iterable object are true, false otherwise

langs = ["java", "php", "python", ""]

print("> all:")

if(all(langs)):
    print("All set")
else:
    print("Not all set")

print("=" * 48)


## any(iterable): returns true if at least one element of the iterable object is true, false otherwise

myList = [0, ""]

print("> any:")

if(all(myList)):
    print("All set")
else:
    print("Not all set")

print("=" * 48)

## bin(integer): transform to binary code

print("> bin:")

print(bin(100))
print(bin(-20))

print("=" * 48)


## id(object): returns the address of the given object

print("> id:")

print(id(langs))
print(id(myList))
print(id("java"))

print("=" * 48)


## sum(iterable [, start = 0]): return the sum of the given iterable object, can specify the starting number of the sum

print("> sum:")

numbers = [ 2, 4, 8, 16]
print(sum(numbers))
print(sum(numbers, 32))

print("=" * 48)

## round(number, digits)

print("> round:")

print(round(3.1403758))
print(round(3.145687, 2))

print("=" * 48)


## range([start,] end [,step])

print("> range:")

print(list(range(0)))
print(list(range(8)))
print(list(range(4,16,2)))

print("=" * 48)

## print() // , is like a separator

print("> print:")

print("Hello","World")
print("Hello","world", sep="_") # default sep = " "
print("Line one", end= ",")
print("Line two")

print("=" * 48)

## abs(number)

print("> print:")

print(abs(-100))
print(abs(-32.6))
print(abs(20))

print("=" * 48)


## pow(base, expo, mod)

print("> pow:")

print(pow(2,4))
print(pow(3, 4, 5)) # (3*3*3*3)%5

print("=" * 48)


## min(iterable)

print("> min:")

numbers = [3, 4, 5, 12, 8]
print(min(*numbers))

## max(iterable)

print("> max:")

print(min(*numbers))

print("=" * 48)


## slice([start, ]stop)

print("> slice:")

print(numbers[slice(3)])
print(numbers[slice(3,10)])

print("=" * 48)


## map(function, iterable)

print("> map:")

def setCapital(text):
    return text.strip().lower().capitalize()

langs = [ "JaVa", "PyThon", "pHp", "c"]

langsCaps = map(setCapital, langs)

for lang in langsCaps:
    print(f"- {lang}")

print("=" * 48)

### With a lambda function:

for lang in list(map( lambda text: text.strip().lower().capitalize(), langs)):
    print(f"- {lang}")

print("=" * 48)


## filter(function, iterable): function must return a boolean value

print("> filter:")

numbers = [ 0, 3, 15, 7, 8, 0, 12]

def filterNumbers(num):
    return num != 0

result = filter(filterNumbers, numbers)

for number in result:
    print(number)

print("=" * 48)

langs = [ "Java", "Python", "JavaScript", "PHP", "C++"]

for lang in list(filter(lambda lng : lng.lower().startswith("j"), langs)):
    print(lang)

print("=" * 48)


## reduce(function, iterable): function take 2 args(elements) from the iterable

from functools import reduce

print("> reduce:")

def getMyLangsString(lang1, lang2):
    return lang1 + "_" + lang2

result = reduce(getMyLangsString, langs)

print(result)

print("=" * 48)


## enumerate(iterable, start=0): assign enumeration to the iterable obejct

print("> enumerate:")

result = enumerate(langs,1)

for counter, lang in result:
    print(f"{counter} => {lang}")

print("=" * 48)

## help(funct)

print("> help:")

#help()

print("=" * 48)


## reversed(iterable)

print("> reversed:")

name = reversed("adda meceffeuk")

for l in name:
    print(l, end="")

