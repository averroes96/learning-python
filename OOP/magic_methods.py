class Skill:

    def __init__(self, skills): # Constructor
        self.skls = skills

    def __str__(self): # toString
        return f"My Skills: {self.skls}"

    def __len__(self): # length
        return len(self.skls)

        
profile = Skill([ "Java", "Python", "C", "PHP"])

print(profile.__class__) # __class__: magic methods that returns the class name of the instance

print(profile) # Will call __str__ method

print(len(profile))

