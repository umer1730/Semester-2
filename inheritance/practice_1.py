class Animal:
    def sound(self):
        print("wao wao")
class Dog(Animal):
    def sound(self):
        print("Woof Woof")
anm = Dog()
anm.sound()

print()
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
class Car(Vehicle):
    def __init__(self, brand, model,seats):
        super().__init__(brand,model)
        self.seats = seats
    def details(self):
        print(f"{self.brand} model name {self.model} and {self.seats}")        
c = Car("Toyota","Corolla",4)
c.details()

print()
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return 3.14*self.r*self.r
class Recangle(Shape):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
print(Circle(5).area())    
print(Recangle(5,3).area())    

print()
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no = roll_no
    def details(self):
        print(f"Name: {self.name} \nAge: {self.age} \nRoll No: {self.roll_no}")
s1 = Student("Ali",23,2)
s1.details()
        
print()
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if amount > 0:
            self.balance -= amount
        else:
            print("Invalid amount")
class SavingAccount(BankAccount):
    def __init__(self,balance,interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += self.balance * self.interest_rate
acc = SavingAccount(10000,0.5)
acc.add_interest()
print(acc.balance)

print()
class LivingThing:
    def __init__(self):
        print("Living thing created")
class Animal(LivingThing):
    def __init__(self):
        super().__init__()
        print("Animal created")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
Dog()

print()
class Employee:
    def get_salary(self):
        return 0
class Manager(Employee):
    def get_salary(self):
        return 80000
class Developer(Manager):
    def get_salary(self):
        return 100000
print(Employee().get_salary())
print(Manager().get_salary())
print(Developer().get_salary())

print()
class Book:
    def __init__(self, title):
        self.title = title
    def display(self):
        print("Book title:", self.title)
class EBook(Book):
    def __init__(self, title, filesize):
        super().__init__(title)
        self.filesize = filesize
    def display(self):
        print(f"E-Book: {self.title}, File Size: {self.filesize}MB")
class PrintedBook(Book):
    def __init__(self, title, pages):
        super().__init__(title)
        self.pages = pages
    def display(self):
        print(f"Printed Book: {self.title}, Pages: {self.pages}")
Book("C++").display()
EBook("Python", 5).display()
PrintedBook("Math", 300).display()

print()
class Mother:
    def skills(self):
        print("cooking")
class Father:
    def skills(self):
        print("Working")
class Child(Mother,Father):
    def skills(self):
        super().skills()
        print("Studying")
c = Child()
c.skills()

print()
class Person:
    def __init__(self,name):
        self.name = name
    def info(self):
        print(f"Name:  {self.name}")
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        print(f"Teacher's name: {self.name}, Subject: {self.subject}")
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade
    def info(self):
        print(f"Student's name: {self.name}, Grade: {self.grade}")
intro = Person("Ali")
intro.info()
intro = Teacher("Arslan","Physics")
intro.info()
intro = Student("Uzair",10)
intro.info()

print()
class GrandParent:
    def family(self):
        return "Smith"
class Parent(GrandParent):
    def parent(self):
        return "From parent"
class Child(Parent):
    def child(self):
        return "From child"
c = Child()
print(c.child())
print(c.parent())
print(c.family())