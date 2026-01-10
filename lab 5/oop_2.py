class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Person {self.name} is created")
    def __del__(self):
        print(f"Person {self.age} is destroyed")
p = Person("Alice",25)
del p

print()
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
s1 = student("Rabia",60)
s2 = student("Fatima",40)
del s2
del s1.name
print(s1.marks)

class Book:
# Constructor
    def __init__(self, name):
        self.name = name
        print(f"Constructor: Book {self.name} created")
# Destructor
    def __del__(self):
        print(f"Destructor: Book {self.name} destroyed")
# Create an object
b = Book("poems")
# Delete the object
del b

print()
class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def move(self):
        print(f"{self.brand} moves with {self.speed}Km/h speed")
class Car(Vehicle):
    def __init__(self,brand,speed,fuel_types):
        super().__init__(brand,speed)
        self.fuel_types = fuel_types
    def move(self):
        print(f"{self.brand} moves with {self.speed}Km/h speed and consumes {self.fuel_types} fuel")
c = Car("Toyata",200,"1 litres")
c.move()

v = Vehicle("Suzuki",100)
c.move()
