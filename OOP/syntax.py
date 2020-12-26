# Class : BluePrint or constructor of the object

class Member:

    # Class my have attrs and methods
    # __init__ method is called every time we instantiate the class

    notAllowedNames = ["fuck", "shit", "dick", "pussy"]
    
    def __init__(this, firstName, lastName, gender) -> None: # Self refer to the current instance of the class
        super().__init__()
        
        if not Member.isAllowed(firstName.lower()):
            raise ValueError("This name is not allowed")

        this.name = firstName # Instance attribute
        this.last = lastName # Instance attribute
        this.gender = gender.lower() # Instance attribute

    def getFullName(this): # Instant method
        return f"{this.name.lower().capitalize()} {this.last.lower().capitalize()}"

    def sayHello(this):
        if this.gender == "male":
            return f"Hello Mr {this.name.lower().capitalize()}"
        elif this.gender == "female":
            return f"Hello Miss {this.name.lower().capitalize()}"
        else:
            return f"Hello freak {this.name.lower().capitalize()}"

    @classmethod
    def isAllowed(cls, name): # Class method preceded by @classmethod
        if name in cls.notAllowedNames:
            return False
        else:
            return True

    @staticmethod
    def doSomething(): # Static metho, can accept zero parameter
        print("I'm just a static method!")

ada = Member("Ada", "Meceffeuk", "MALE")
randa = Member("Randa", "Meceffeuk", "FemaLe")
justin = Member("Justin", "Bieber", "Binary")
#retard = Member("john", "DICK", "Binary") : example to show how to use class attrs with instant attrs, will raise a valueError

print(ada.__class__) # get the instant's class
print(ada.name)
print(ada.getFullName())

print("=" * 48)

print(ada.sayHello())
print(randa.sayHello())
print(justin.sayHello())

Member.doSomething()

