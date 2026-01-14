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

print()
from abc import ABC, abstractmethod
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass
class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)
class MergeSort(SortStrategy):
    def sort(self, data):
        return sorted(data)
class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    def set_strategy(self, strategy):
        self.strategy = strategy
    def sort(self, data):
        return self.strategy.sort(data)
s = Sorter(QuickSort())
print(s.sort([5, 2, 8]))
s.set_strategy(MergeSort())
print(s.sort([5, 2, 8]))


print()
class Bird:
    pass
class FlyingBird(Bird):
    def fly(self):
        print("Flying")
class Penguin(Bird):
    def swim(self):
        print("Swimming")
class Sparrow(FlyingBird):
    pass
f = FlyingBird()
f.fly()

print()
class Device:
    def __init__(self, brand, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        print(f"Device {self.brand} initialized.")

class WiFiConnected:
    def __init__(self, ip_address, **kwargs):
        super().__init__(**kwargs)
        self.ip_address = ip_address
        print(f"Connected to {self.ip_address}.")

class SmartCamera(Device, WiFiConnected):
    def __init__(self, brand, ip_address, resolution):
        super().__init__(brand=brand, ip_address=ip_address)
        self.resolution = resolution

cam = SmartCamera("Sony", "192.168.1.1", "4K")
print("Order of search:", SmartCamera.__mro__)