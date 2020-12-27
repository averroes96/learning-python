from math import pi
 
class Shape: # Parent class

    def calculateSurface(self):
        raise NotImplementedError("Method not implemented yet")

    def calculatePerimeter(self):
        raise NotImplementedError("Method not implemented yet")

class Triangle(Shape):

    def __init__(self, base, side_a, side_c, height):
        self.base = base
        self.side_a = side_a
        self.side_c = side_c
        self.height = height

    def calculateSurface(self):
        return f"Surface = {(self.base * self.height)/2}"
        

    def calculatePerimeter(self):
        return f"Perimeter = {(self.base + self.side_a + self.side_c)}"

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculateSurface(self):
        return "Surface = " + str(pi * (self.radius ** 2))
        

    def calculatePerimeter(self):
        return "Perimeter = " + str(2 * pi * self.radius)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateSurface(self):
        return "Surface = " + str(self.width * self.height)
        

    def calculatePerimeter(self):
        return "Perimeter = " + str(2 * (self.width + self.height))


triangle = Triangle(4,3,3,2.5)
circle = Circle(2.5)
rectangle = Rectangle(5,3)

print(triangle.calculateSurface())
print(circle.calculateSurface())
print(rectangle.calculateSurface())

print(triangle.calculatePerimeter())
print(circle.calculatePerimeter())
print(rectangle.calculatePerimeter())