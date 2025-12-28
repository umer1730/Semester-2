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