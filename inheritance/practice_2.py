class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Electronics(Product):
    def __init__(self,name,price,waranty):
        super().__init__(name,price)
        self.waranty = waranty
    def info(self):
        print(f"Product: {self.name}, Price: ${self.price}, Waranty: {self.waranty} years")
class Clothing(Product):
    def __init__(self,name,price,size,material):
        super().__init__(name,price)
        self.size = size
        self.material = material
    def info(self):
        print(f"Product: {self.name},Price: ${self.price}, Size: {self.size}, Material: {self.material}")
c = Electronics("Laptop",10000,2)
c.info()
c = Clothing("Shirt",2000,"M","Cotton")
c.info()

print()
class Dog:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.sleep} is sleeping")
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.sleep} is sleeping")
d = Dog("Bull dog",22)
d.eat()
d.sleep()
c = Cat("meow",12)
c.eat()
c.sleep()

print()
# so we use inheritance method
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Dog(Animal):
    pass
d = Dog("Buddy",3)
d.eat()
d.sleep()

print()
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Dog(Animal):
    def bark(wolf):
        print("woof")
d = Dog("buddy",3)
d.eat()
d.sleep()
d.bark()

print()
class Animal:
    def breathe(self):
        print(f"{self} is breathing")
class Dog(Animal):
    pass
d = Dog()
d.breathe()

print()
class Animal:
    def breathe(self):
        print(f"{self} is breathing")
class Dog(Animal):
    def bark(self):
        print("Woof woof!")
    def wag_tail(self):
        print("Tail wagging happily")
d = Dog()
d.bark()
d.breathe()

print()
class Animal:
    def speak(self):
        print("Some sound")
class Cat(Animal):
    pass
class Dog(Animal):
    def speak(self):
        print("woof")
d = Dog()
d.speak()
c = Cat()
c.speak()

print()
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Dog(Animal):
    def __init__(self,name,age,breed):
        Animal.__init__(self,name,age)
        self.breed = breed
d =  Dog("Buddy",2,"coco")
print(d.breed)

print()
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.species = "Unknown"
        self.is_alive = True
        self.energy = 100
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed
d = Dog("Dude", 2, "German Shepherd")
print(d.name, d.age, d.breed, d.is_alive)

print() 
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)   # hm super method me parent class ko child class ke andr call krwane ke liye use krte ha
        self.breed = breed
    def eat(self):
        super().eat()
        print(f"{self.name} is chewing on a bone")
d = Dog("Buddy",2,"Unknown")
d.eat()

print()
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age =  age
        print(f"Animal {self.name} created")
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed
        print(f"It's a {self.breed}")
    def bark(self):
        print("Woof woof")
d = Dog("Buddy",3,"Golden retriever")
d.eat()
d.bark()

print()
class Animal:
    def breathe(self):
        print("Breathing.....")
class Mammal(Animal):
    def specifies(self):
        print("have backbone")
class Dog(Mammal):
    def bark(self):
        print("Woof!")
d = Dog()
d.bark()
d.breathe()
d.specifies()

print()
class Animal:
    def __init__(self,name):
        self.name = name
        print("Animal init")
class Mammal(Animal):
    def __init__(self,name,has_fur):
        super().__init__(name)
        self.has_fur = has_fur
        print("Mammal init")
class Dog(Mammal):
    def __init__(self,name,has_fur,breed):
        super().__init__(name,has_fur)
        self.breed = breed
        print("Dog init")
d = Dog("Max",True,"German shephered")

print()
class Animal:
    def speak(self):
        print("Some sound")
class Mammal(Animal):
    def speak(self):
        print("Mammal sound")
class Dog(Mammal):
    def speak(self):
        print("woof!")
d = Dog()
d.speak()

print()
class Animal:
    def speak(self):
        print("Some sound")
class Mammal(Animal):
    def speak(self):
        print("Mammal sound")
class Dog(Mammal):
    def speak(self):
        super().speak()
        print("woof")
d = Dog()
d.speak()

print()
class Car:
    def  __init__(self,brand):
        self.brand  =  brand
        print(f"Car initialized: {self.brand}")
    def start_engine(self):
        return "Engine started"
class PetrolCar(Car):
    def __init__(self,brand,tankcapacity):
        super().__init__(brand)
        self.tankcapacity = tankcapacity
        print(f"Petrolcar initialized with {self.tankcapacity} litres tank")
class ElectricCar(Car):
    def __init__(self,brand,battery_size):
        super().__init__(brand)
        self.battery_size = battery_size
        print(f"ElectricCar initialized with {self.battery_size} KWh battery")
    def charge(self):
        return "Charging the elctric battery"
class TeslaModel3(ElectricCar):
    def autopilot(self):
        return "Autopilot engaged"
my_tesla = TeslaModel3("Tesla",75)
print(my_tesla.start_engine())
print(my_tesla.charge())
print(my_tesla.autopilot())