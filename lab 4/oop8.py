class Car:
    def __init__(self,brand):
        self.brand = brand
        print(f"Car brand is {self.brand}")
c1 = Car("Bugatti")
c2 = Car("Mercedes")

print()
print("-------student data-----")
class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks
    def is_passed(self):
        
        if self.marks >= 50:
            print("Pass")
        else:
            print("Fail")
name = input("Enter name: ")
marks = int(input("Enter marks: "))
s1 = Student(name,marks)            
s1.is_passed()

print()
print("-----table----")
class Table:
    def __init__(self,num):
        self.num = num
    def print_table(self):
        for i in range(1,11):
            print(f"{self.num} x {i} = {self.num * i}")
n = int(input("Enter number: "))
t = Table(n)
t.print_table()

print()
print("-----bank----")
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance: {self.balance}")
account = BankAccount(500)
while True:
    action = input("\nEnter 'd' to deposit, 'w' to withdraw, 'exit' to quit: ")
    if action =="exit":
        print("Thankyou for using our bank!")
        break
    elif action == "d":
        amt = float(input("Enter deposit amount: "))
        account.deposit(amt)
    elif action == "w":
        amt = float(input("Enter withdrawl amount: "))
        account.withdraw(amt)
    else:
        print("Invalid choice!")

print()
print("----employee-------")
class Employee:
    company = "ABC Pvt Ltd"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {Employee.company}")
e1 = Employee("ALi",20000)
e2 = Employee("Sara",10000)
e3 = Employee("Arslan",5000)
e1.display_info()
e2.display_info()
e3.display_info()
Employee.company = "XYZ Ltd"
print("After changing company name: ")

print()
print("------temp------")
class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
        if self.celsius < 0:
            print("Freezing point reached!")
    def method_to_fahrenheit(self):
        f = (self.celsius*9/2)+32
        return f
value = float(input("Enter value: "))
v1 = Temperature(value)
print(f"Temperature in fahrenheit: {v1.method_to_fahrenheit():.2f}")


