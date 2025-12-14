from abc import ABC,abstractmethod
class Bank_Account(ABC):
    @abstractmethod
    def check_balance(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class Current_account(Bank_Account):
    def __init__(self,balance = 100):
        self.balance = balance
    def check_balance(self):
        print(f"Current balance is: {self.balance}")

    def deposit(self,amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposited amount is: {self.balance}")
        else:
            print("Price can not be negative")

    def withdraw(self,amount):
        if amount >= 0:
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print(f"Withdrawn amount. New balance: {self.balance}")
        else:
            print("Amount cannot be negative")
    
class Savings_account(Bank_Account):
    profit = 0.05
    def check_balance(self,balance = 100):
        self.balance = balance
        total = self.balance + (self.balance * Savings_account.profit)
        print(f"Saving balance is: {total}")
    
    def deposit(self,amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposited amount is: {self.balance}")
        else:
            print("Price can not be negative")

    def withdraw(self,amount):
        if amount >= 0:
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print(f"Withdrawn amount. New balance: {self.balance}")
        else:
            print("Price cannot be negative")

#initial balance
current_acc = Current_account()
savings_acc = Savings_account()

current_acc.check_balance()
savings_acc.check_balance()

current_acc.deposit(50)
savings_acc.deposit(100)

current_acc.check_balance()
savings_acc.check_balance()

        