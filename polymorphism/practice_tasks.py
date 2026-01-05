class Dog:
    def sound(self):
        return "Bark"
class Cat:
    def sound(self):
        return "Meow"
animals = [Dog(),Cat()]
for a in animals:
    print(a.sound())

print()
class Bird:
    def fly(self):
        return "Birds can fly"
class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"
b1 = Bird()
b2 = Bird()
print(b1.fly())
print(b2.fly())

print()
class Car:
    def move(self):
        return "Car is driving"
class Plane:
    def move(self):
        return "Plane is flying"
def start(obj):
    print(obj.move())
start(Car())
start(Plane())

print()
print(10+5)
print("Ali"+"Agha")
print([1,2],[3,4])

print()
print(len("Hello"))
print(len([1,2,3,4]))
print(len({"a":10,"b":20}))

print()
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,side):
        self.side  = side
    def area(self):
        return self.side * self.side
s = Square(4)
print(s.area()) 

print()
class Vehicle:
    def speed(self):
        print("Vehicle speed")
class Car(Vehicle):
    def speed(self):
        print("Car speed is 120 Km/h")
v = Car()
v.speed()