# Promotes code reusability by sharing attributes and methods across classes.
class Animal:
    def __init__(self,name):
        self.name = name
    def info(self):
        print("Animal name:", self.name)
class Dog(Animal):
    def sound(self):
        print(self.name, "barks")
d = Dog("Buddy")
d.info()
d.sound()

print()
# super() function is used to call the parent class’s methods. In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes
class Animal:
    def __init__(self,name):
        self.name = name
    def info(self):
        print("Animal name: ",self.name)
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def details(self):
        print(f"{self.name} is a {self.breed}")
d = Dog("Buddy","Golden Retriever")
d.info()
d.details()

print()
# In single inheritance, a child class inherits from just one parent class.
class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def show_role(self):
        print(f"{self.name} is an employee")
emp = Employee("Sarah")
print("Name: ", emp.name)
emp.show_role()

print()
# In multiple inheritance, a child class can inherit from more than one parent class.
class Person:
    def __init__(self,name):
        self.name=name
class Job:
    def __init__(self,salary):
        self.salary = salary
class Employee(Person,Job):
    def __init__(self,name,salary):
        Person.__init__(self,name)
        Job.__init__(self,salary)
    def details(self):
        print(self.name," earns", self.salary)
emp = Employee("Ali",40000)
emp.details()

print()
#In multilevel inheritance, a class is derived from another derived class (like a chain)
class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def show_role(self):
        print(f"{self.name} is an employee")
class Manager(Employee):
    def department(self,dept):
        print(f"{self.name} manages {dept} department")
mgr = Manager("Joy")
mgr.show_role()
mgr.department("HR")

print()
#In hierarchical inheritance, multiple child classes inherit from the same parent class
class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def role(self):
        print(f"{self.name} works as an employee")
class Intern(Person):
    def role(self):
        print(self.name,"is an intern")
emp= Employee("David")
emp.role()
int = Intern("Eva")
int.role()

print()
#Hybrid inheritance is a combination of more than one type of inheritance
class Person:
    def __init__(self,name):
        self.name = name
class employee(Person):
    def role(self):
        print(self.name, "is an employee")
class Project:
    def __init__(self,project_name):
        self.project_name = project_name
class TeamLead(Employee,Project):
    def __init__(self, name,projet_name):
        Employee.__init__(self,name)
        Project.__init__(self,projet_name)
    def details(self):
        print(self.name, "leads project:" ,self.project_name)
lead = TeamLead("Sara","AI Development")
lead.role()
lead.details()