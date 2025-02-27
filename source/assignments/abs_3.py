from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

# Instantiate and print areas
rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"Area of Rectangle: {rectangle.area()}")
print(f"Area of Circle: {circle.area()}")
