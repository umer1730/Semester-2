class Calculator:
    def multiply(self, a =1,b=1,*args):
        result = a*b
        for num in args:
            result *= num
        return result
calc = Calculator()
print(calc.multiply())
print(calc.multiply(4))

print(calc.multiply(4,3))
print(calc.multiply(4,3,2))
print()
class Animal:
    def sound(self):
        return "Some generic sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"
animals = [Dog(),Cat(),Animal()]
for animal in animals:
    print(animal.sound())

print()
print(len("Hello"))
print(len([1,2,3,4]))
print(max(1,2,3))
print(max("H","e","l","l","o"))

print()
class Pen:
    def use(self):
        return "Erasing"
class Eraser:
    def use(self):
        return "Writing"
def perform_task(tool):
    print(tool.use())
perform_task(Pen())
perform_task(Eraser())

print()
print(5+10)
print("Hello"+ "World!")
print([1,2] + [3,4])

print()
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Point(self.x + other.x,self.y + other.y)
p1 = Point(2,3)
p2 = Point(4,5)
p3 = p1+p2
print(p3.x,p3.y)

print()
class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return self.pages+other.pages
b1 = Book(100)
b2  = Book(250)
print(b1 + b2)

print()
class Student:
    def __init__(self,marks):
        self.marks = marks
    def __gt__(self,other):
        return self.marks > other.marks
s1 = Student(85)
s2 = Student(92)
print(s1>s2)
print(s2>s1)

print()
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y= y
    def __str__(self):
        return f"Point({self.x},{self.y})"
p = Point(3,4)
print(p)

print()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
p1 = Point(2, 3)
p2 = Point(4, 20)
print(p1 / p2)
