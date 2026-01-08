class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def display_info(self):
        print(f"The person name is {self.__name} and the age is {self.__age}")
p1 = Person("ali",25)
p1.display_info()
# p1.__name    # in protected it can only be derived in the derived class
# p1.__age


class Employee:
    def __init__(self):
        self.name = "Ali"
        self._salary = 5000
        self.__bonus = 500
emp = Employee()
print(emp.name)
#print(emp._salary)  accessible but not recommended
#print(emp._Employee__bonus)  works but not recomended


print()
print("---next---")
class Employee:
    company = "Netsol"
    def __init__(self,name,salary,bonus):
        self.name = name
        self._salary = salary
        self.__bonus = bonus
    def display_info(self):
        print(f"Company: {Employee.company}")
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"Bonus: {self.__bonus}")
emp = Employee("Ali",50000,1500)
emp.display_info()
print(emp._salary) # accessible but not recommended


print()
print("----next----")
class Student:
    def __init__(self,grade):
        self.__grade = grade 
        if grade > 0:
            self.__grade
        else:
            0
    def get_grade(self):
        return self.__grade
    def set_grade(self,value):
        if value >= 0 and value <= 100:
            self.__grade = value
s = Student(85)
print(s.get_grade())
s.set_grade(90)
print(s.get_grade())


print()
print("---next---")
class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age= age
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age!")
s = Student("Ali",20)
print("Name:", s._Student__name) # direct access not recommended
print("Age:",s.get_age())
s.set_age(34)
print("Updated age: ", s.get_age())        


print()
print("----next----")
class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    @property
    def get_age(self):
        return self.__age 
    @get_age.setter
    def get_age(self,new_age):
        if new_age > 0:
            self.__age = new_age 
        else:
            print("Invalid age can not be negative")
s = Student("ali",20)
print("Age: ",s.get_age)
s.get_age = 34
print("Updated age: ",s.get_age)
s.get_age = -2


print()
print("----next----")
class Employee:
    def __init__(self,salary):
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,amount):
        if amount >= 0:
            self.__salary = amount
        else:
            print("Salary can't be negative")
emp = Employee(5000)
print("Salary: ",emp.salary)
emp.salary = 6000
print("Updated salary:", emp.salary)
emp.salary = -1000


print()
class StockMarket:
    def __init__(self):
        self.observers = []
        self.price = 0
    def subscribe(self,observer):
        self.observers.append(observer)
    def set_price(self,price):
        self.price = price
        for obs in self.observers:
            obs.update(price)
class MobileApp:
    def update(self,price):
        print("Mobile app notify")
class Webapp:
    def update(self,price):
        print("Web app notified")
market  =StockMarket()
market.subscribe(MobileApp())
market.subscribe(Webapp())
market.set_price(500)