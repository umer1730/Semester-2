class Student:
    def __init__(self,marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if marks >=0 and marks <=100:
            self.__marks = marks
        else:
            print("invalid")
s = Student(80)
print(s.get_marks())
s.set_marks(150)

print()
print("----next----")
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid amount , can't be neg")
    def deposit(self,amount):
        self.__balance += amount
        print("Deposited: ",amount)
    def withdrawn(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Withdrawn: ",amount)
        else:
            print("Indsuficient amount")
b = BankAccount(1000)
b.deposit(200)
b.withdrawn(300)
print(b.balance)

print()
class Person:
    def __init__(self,name):
        self.name = name
        print(f"Constructor: {self.name} created")
    def __del__(self):
        print(f"Destructor: {self.name} destroyed")
p =Person("ali")
del p

print()
class FileHandler:
    def __init__(self,filename):
        self.filename = filename
        print(f"{self.filename} open")
    def __del__(self):
        print(f"{self.filename} close")
f = FileHandler("data.txt")
del f

print()
class Timer:
    def __init__(self,time):
        self.time = time
        print(f"{self.time} starts")
    def __del__(self):
        print(f"{self.time} stops")
t = Timer(12)
del t

print()
class Patient:
    def __init__(self,name,age,disease):
        self.__name = name
        self._age = age
        self.__disease = disease
    def show_record(self):
        print(f"Name: {self.__name} \nAge: {self._age} \nDisease: {self.__disease}")
p = Patient("Ali",24,"Flu")
p.show_record()

print()
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary= salary
        self._department = "HR"
    def show_salary(self):
        print(f"Salary: {self.__salary}")
    def set_salary(self,new_salary):
        if new_salary >= 0:
            self.__salary  = new_salary
        else:
            print("salary can't be neg")
e = Employee("ali",40000)
e.show_salary()
e.set_salary(60000)
e.show_salary()

print()
