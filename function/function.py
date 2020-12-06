# Declatation def <name> :

def function_name():
    print("I'm function")

print("=" * 48)


# Call
function_name()

def return_func():
    return "I'm function"

print(return_func())

print("=" * 48)


### Args and params

# name = input("Enter your name:\t").strip().lower().capitalize()

def sayHello(name):
    print("Hello " + name)

sayHello("Ada")

print("=" * 48)

def addition(a, b):
    if(str(a).isnumeric() & str(b).isnumeric()):
        return int(a) + int(b)
    else:
        return "Numeric only you deep shit!"

print(addition("dsfsf", 50))

### Packing, Unpacking args

def sayHello(*names):
    for name in names:
        print(f"Hey {name}")

sayHello("Averroes", "Epicurus", "Ada") # Undefined number of args ( can be 0 )

print("=" * 48)


### Default params

def sayHello(name, age, country = "Undefiend"):

    print(f"Name:\t {name.lower().capitalize()}")
    print(f"Age:\t {age}")
    print(f"Country:\t {country.lower().capitalize()}")

print(sayHello("Ada", 24, "DZ"))

print("=" * 48)



### Unpacking keyword

def getSkills(**dict): # ** implies dictionary * implies list|tuple|set
    
    for key, value in dict.items():
        print(f"{key} => {value}")

mySkills = {
    "Java" : "85%",
    "PHP" : "70%",
    "C" : "60%"
}

getSkills(**mySkills)

print("=" * 48)


### Global/Local scope

x = 1 # global scope

def myfunc():
    
    # local scope
    x = 2
    print(x)


def myfunc2():

    # override a globale variable
    global x
    x = 5
    print(x)

myfunc()
print(x)
myfunc2()
print(x)