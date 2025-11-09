class Rectangle:
    def set_dimensions(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
rect = Rectangle()
rect.set_dimensions(4, 5)
print(f"Area: {rect.area()}")

print()
print("----next-----")
class Rectangle:
    def set_dimensions(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 * (self.length+self.width)
rect = Rectangle()
rect.set_dimensions(4, 5)
print(f"Perimeter: {rect.perimeter()}")


print()
print("---next-----")
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
student1 = Student("Ali",24)
student2 = Student("Sara",23)
print(student1.name,student1.age)
print(student2.name,student2.age)

print()
print("----next------")
class Dog:
    def __init__(self,name,breed = "unknown",age=1):
        self.name = name
        self.breed = breed
        self.age = age
dog1 = Dog("Buddy")
dog2 = Dog("Max","Labrador")
dog3 = Dog("Bella","Poodle",3)
print(dog1.breed)
print(dog2.breed)

print()
print("-----next----")
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calc_distance(self,other):
        return math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)
p1 = Point(2,2)
p2 = Point(6,5)
print("P1-x, P1-y is:", p1.x, p1.y)
print("P2-x, P2-y is:", p2.x, p2.y) 
print("Distance from P1 to P2 is:", p1.calc_distance(p2))
