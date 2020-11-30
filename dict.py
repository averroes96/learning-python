# Dict's items are inside a curly brackets
# Item = key + value
# Keys must be unique and accept just immutable values
# Values can be any type of data

myDict = {
    "name" : "Ada Meceffeuk",
    "age" : 24,
    "Nationality" : "Algerian",
    "Languages" : [ "Arabic", "English", "French"]
}

print(type(myDict))

print("=" * 48)

### Accessing an item by key

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

print(car.get("model"))
print(car["model"])

print("=" * 48)

### Getting all keys and values

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.keys()
car['color'] = 'white'
print(x)

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.values()
car['year'] = 2018
print(x)

print("=" * 48)

### Two dim dictionaries

langs = {
    "Java" : {
        "progress" : "80%",
        "years" : 3
    },
    "PHP" : {
        "progress" : "70%",
        "years" : 2
    },
    "C" : {
        "progress" : "60%",
        "years" : 4
    }

}

print(langs)
print(langs["Java"])
print(langs["C"]["progress"])

print("=" * 48)

### Creating dict from variables

java = {
    "progress" : "80%",
    "years" : 3
}

php = {
    "progress" : "70%",
    "years" : 2
}

langs = {
    "java" : java,
    "php" : php
}

print(type(langs))
print(langs["java"])

print("=" * 48)

### Methods: clear()

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
car.clear()
print(car)

print("=" * 48)

### Methods: update()

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
car.update({'color': 'White'}) # or car['color] = 'white'
print(car)

### Methods: copy()

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.copy()
print(x)

### Methods: setdefault() // check if key exists, if it doesn't it init it with the given value

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.setdefault('color', 'white')
print(car)

print("=" * 48)

### Methods: popitem() // Returns the last item and remove it from the dict

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
car.popitem()
print(car)

print("=" * 48)

### Methods: items()

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.items()
car['year'] = 2018
print(x)

print("=" * 48)

### Methods: fromkeys() // creates a dict from a given tuple of keys

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)
