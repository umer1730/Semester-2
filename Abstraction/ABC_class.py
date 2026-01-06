from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
r = Rectangle(4, 5)
c = Circle(3)

print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

print()
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass
    def sleep(self):
        print("sleeping")
class Dog(Animal):
    def make_sound(self):
        print("Wooof")
    def move(self):
        print("returning")
dog = Dog()
dog.make_sound()
dog.move()
dog.sleep()


print()
from abc import ABC,abstractmethod
import math
class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
Shape = [Rectangle(3,4),Circle(2)]
for i in Shape:
    print(i.area())