# create bank account class in encapsulatiton
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount >= 0:
            self.__balance += amount
            print(f"Balance after depositing amount is: {self.__balance}")
        else:
            print("Invalid! amount cannot be negative. It must be greater then zero")
    def withdraw(self,amount):
        if amount >= 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Balance after withdrawn amount is: {self.__balance}")
        else:
            print("Invalid! amount can never be negative")
    
bank = BankAccount(12000)
bank.deposit(200)
bank.withdraw(1000)
print("Final Balance: ",bank.get_balance())

# create appliances method in abstraction
print()
from abc import ABC,abstractmethod
class Appliance:
    @abstractmethod
    def turn_on(self):
        pass
class Washing_machine(Appliance):
    def turn_on(self):
        print("Washing machine is starting")
        print("Locking door")
        print("Filling wter")
class Television(Appliance):
    def turn_on(self):
        print("Television is starting")
        print("Displaying logo")
        print("Loading channels")
was = Washing_machine()
was.turn_on()

tv = Television()
tv.turn_on()  

# create classs in inheritance
class Employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
class Manager(Employee):
    def __init__(self,name,employee_id,team_size):
        super().__init__(name,employee_id)
        self.team_size = team_size
    def show_info(self):
        print(f"Name: {self.name} \nEmployee ID: {self.employee_id} \nTeam size: {self.team_size}")
class Developer(Employee):
    def __init__(self,name,employee_id,programming_language):
        super().__init__(name,employee_id)
        self.programming_language = programming_language
    def show_info(self):
            print(f"Name: {self.name} \nEmployee ID: {self.employee_id} \nProgramming language: {self.programming_language}")
manger = Manager("Ali","M24",50)
manger.show_info()

developer = Developer("Arslan","D24","Python")
developer.show_info()