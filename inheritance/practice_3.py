class Animal:
    def sound(self):
        print("Animal can not talk")
class Dog(Animal):
    def sound(self):
        print("Dog bark")
d = Dog()
d.sound()

print()
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def display_info(self):
        super().display_info()
        print(f"Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, age, salary, experience):
        super().__init__(name, age, salary)
        self.experience = experience
    def display_info(self):
        super().display_info()
        print(f"Experience: {self.experience} years")
p = Manager("Ali", 30, 12222, 3)
p.display_info()

p = Employee("Ali",12,1133333)
p.display_info()

print()
class Vehicle:
    def __init__(self,name,model):
        self.name = name
        self.model = model
class Car(Vehicle):
    def info(self):
        print(f"{self.name} model is {self.model}")
class Bike(Vehicle):
    def info(self):
        print(f"{self.name}'s {self.model}")
c= Car("Toyota","gli")
c.info()
b = Bike("Ninja",2022)
b.info()