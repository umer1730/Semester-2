class Shape:
    def __init__(self,radius):
        self.radius = radius
class Circle(Shape):
    def area(self):
        return 3.14*self.radius*self.radius
c = Circle(78.5)
print(c.area())    

print()

class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def display_info(self):
        print(f"{self.name} is an employee")
class Manager(Person):
    def show_info(self,total):
        print(f"Manager {self.name} manages {total} employes")
m = Manager("John")
m.show_info(5)

print()

class Person:
    def __init__(self,name):
       self.name = name
class Scholar:
    def __init__(self,scholars):
        self.scholars  =scholars
class Student(Person,Scholar):
    def __init__(self, name,scholars):
        Person.__init__(self,name)
        Scholar.__init__(self,scholars)
    def details(self):
        print(f"Student {self.name} has scholarship of {self.scholars}")
s = Student("ALice",5000)
s.details()
    

class Shape:
    def __init__(self,length,width):
        self.length = length
        self.width = width
class rectangle(Shape):
    def area(self):
        return self.length * self.width
r = rectangle(3,4)
print(r.area())

print()
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Teacher(Student):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject
    def info(self):
        print(f"{self.name}\n{self.age}\n{self.subject}")
t = Teacher("Ali",29,"English")
t.info()