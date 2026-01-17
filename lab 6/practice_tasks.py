class Employee:
    def __init__(self,salary):
        self.__salary = salary
    @property
    def get_salary(self):
        return self.__salary
    @get_salary.setter
    def get_salary(self,new_salary):
        if self.__salary >= 15000 and self.__salary <= 200000:
            self.__salary += new_salary
        else:
            print("Invalid salary")
emp =  Employee(50000)
print("Initial salary: ",emp.get_salary)
emp.get_salary = 25000
print("Updated salary: ",emp.get_salary)


print()
print("----2 next---")
class BankAccount:
    def __init__(self,balance,account_no):
        self.__balance = balance
        self.__account_no = account_no
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")
    def withdawn(self,amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient balance")
        else:
            print("Withdrawn amount must be positive")
    def get_balance(self):
        return self.__balance
bank = BankAccount(0,1234)
bank.deposit(5000)
bank.withdawn(2000)
print(bank.get_balance())


print()
print("----3 next----")
class Student:
    def __init__(self,marks):
        self.__marks = marks
    @property
    def get_marks(self):
        return self.__marks
    @get_marks.setter
    def get_marks(self,marks):
        if marks >= 0 and marks <=100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100")
s = Student(95)
print("Marks:",s.get_marks)
s.get_marks = -2


print()
print("----4 next----")
class Product:
    def __init__(self,name,price,stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        if value >=0:
            self.__price = value
        else:
            print("invalid price")
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self,value):
        if value >= 0:
            self.__stock = value
        else:
            print("invalid stock")
    def display_info(self):
        print(f"Product: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Stock: {self.__stock}")
p = Product("Laptop",120000,10)
p.display_info()

p.price = -5000      
p.stock = -3

p.price = 125000     
p.stock = 15     
p.display_info()

print()
class Money:
    def __init__(self,amount,currency):
        self.__amount = amount
        self.__currency = currency
    @property
    def amount(self):
        return self.__amount
    def add(self,other):
        if self.__currency != other.__currency:
            raise ValueError("Currency mismatch")
        return Money(self.__amount + other.__amount,self.__currency)
m1 = Money(100,"USD")
m2 = Money(50, "USD")
m3 = m1.add(m2)
print(m3.amount)

print()
class BankAccount:
    def __init__(self,balance,pin):
        self.__pin = pin
        self.__balance = balance 
        self.count = 0
        self.active = True

    def deposit(self,amount,pin):
        if not self.active:
            print("Account closed")
        if pin == self.__pin:
            print("Correct pin")
            if amount > 0:
                self.__balance += amount
                self.count += 1
                print(f"Your balance after depositing amount is ${self.__balance}")
            else:
                print("Invalid amount")

        else:
            print("Invalid pin")
        
        if self.count == 3:
            self.active = False
            print(f"Account closed, Final balance: {self.__balance}")
        
    def withdraw(self,amount,pin):
        if not self.active:
            print("Account closed")
        if pin == self.__pin:
            print("Correct pin")
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                self.count += 1
                print(f"Your Balance after withdraw amount is ${self.__balance}")
            else:
                print("Invalid amount")
        else:
            print("Invalid pin")
        if self.count == 3:
            self.active = False
            print("Account closed. Final balance:", self.__balance)

    def check_balance(self,pin):
        if not self.active:
            print("Account closed")
        if pin == self.__pin:
            self.count += 1
            return self.__balance
        else:
            print("wrong pin")
        if self.count == 3:
            self.active = False
            print("Account closed. Final balance:", self.__balance)

b = BankAccount(1200,1234)
b.deposit(200,1234)
print(b.check_balance(1234))
b.withdraw(400,1234)

