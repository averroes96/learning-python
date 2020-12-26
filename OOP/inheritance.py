class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Name : {self.name} Email: {self.email}"

class Student(Person):
    def __init__(self, name, email, modules):
        super().__init__(name, email)
        self.modules = modules

    def __str__(self):
        return super().__str__() + f"\nModules: {self.modules}"

modules =  {
    "CV": 12,
    "TAL":11,
    "RCR":14
}

stud = Student("Ada Meceffeuk", "addavigner@gmail.com", modules)

print(stud)