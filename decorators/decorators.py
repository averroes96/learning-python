# Decorator : a function that accepts another function as a parameter

def myDecorator(func):

    def nestedFunc():

        print("=" * 48)

        func()

        print("=" * 48)

    return nestedFunc


@myDecorator
def defineMe():
    print("Hey I'm Ada, Algerian, 23 years old")

defineMe()

# Function with params

def myDecorator(func):

    def nestedFunc(*info):

        print("=" * 48)

        func(*info)

        print("=" * 48)

    return nestedFunc


@myDecorator
def defineMe(*info):
    print(f"Hey I'm {info[0].lower().capitalize()}, I'm from {info[1].capitalize()}, I'm {info[2]} years old")

defineMe("ada", "AlGeria", 23)

# You can use multiple decoartors on the same function

def argsDecoration(func):

    def nestedFunc(*infos):

        for info in infos :
            info.lower().capitalize()

        func(*infos)

    return nestedFunc


@myDecorator
@argsDecoration
def defineMe(*info):
    print(f"Hey I'm {info[0]}, I'm from {info[1]}, I'm {info[2]} years old")