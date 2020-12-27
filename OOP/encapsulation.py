# Public: can be accessed from any file
# Protected: can be accessed from the same class and sub classes (_name)
# Private: can be accessed only from the class (__name)

class Cat:

    def __init__(self, hungry, mood, energy):
        self.hungry = hungry # Public attr
        self._mood = mood # Protected attr
        self.__energy = energy # Private attr

    def _meow(self): # Protected method
        return "Meow !"

    @property
    def getEnergy(self): # Getter
        return self.__energy

    def setEnergy(self, energy): # Setter
        self.__energy = energy

cat = Cat(3,4,8)
print(cat._meow())
print(cat.getEnergy)

cat.setEnergy(7)
print(cat.getEnergy)