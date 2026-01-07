class Employee:
    def __init__(self,name,salary):
        self._name = name
        self._salary = salary if salary >= 0 else 0
    def give_raise(self,amount):
        if amount > 0:
            self._salary += amount
emp = Employee("Alice",50000)
emp.give_raise(1000)
print(emp._salary)
            
print()
print("-----bank-----")
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance if balance >= 0 else 0
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
acc = BankAccount(100)
print(acc.get_balance())
#print(acc.__balance) produce error

print()
print("-----next------")
class Student:
    def __init__(self,grade):
        self.__grade  = grade if grade > 0 else 0
    def get_grade(self):
        return self.__grade
    def set_grade(self,value):
        if 0 <= value <= 100:
            self.grade = value
s = Student(85)
print(s.get_grade())
#s.get_grade(90)
#s.get_grade(150)
#s.__grade=95

print()
print("-----shoping------")
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    def add_item(self,item,price):
        self.items.append(item)
        self.total += price
    def checkout(self):
        if self.total > 0:
            print(f"Payment due: ${self.total}")
cart = ShoppingCart()
cart.add_item("Book",29.99)
cart.checkout()


print()
print("-------next------")
class Wallet:
    def __init__(self,balance):
        self.__balance = balance if balance >= 0 else 0
    def get_balance(self):
        return f"${self.__balance}"
    def set_balance(self,amount):
        if amount >= 0:
            self.__balance = amount
wallet = Wallet(50)

wallet.set_balance(-500)
print(wallet.get_balance())

wallet.set_balance(100)
print(wallet.get_balance())
wallet.__balance = 5000

print()
print("------getters and setters-------")
class Student:
    def __init__(self,grade):
        self.__grade = grade if 0 <= grade <=100 else 0
    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self,value):
        if 0 <= value <= 100:
            self.__grade = value
stud = Student(85)
print(stud.grade)
stud.grade = 90
print(stud.grade) 

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        if amount <= 0:
            raise ValueError("Amount can not be negative")
        self.__balance == amount
acc = BankAccount(500)
acc.balance = 1000
print(acc.balance)