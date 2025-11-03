class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")

b1 = Book("Python","John")
b1.display()

print()
class BankAccount:
    def __init__(self,balance = 0):
        self.balance = balance
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"Deposit: {amount}")
        else:
            print("must be positive")
    def withdraw(self,amount):
        if 0<amount<=self.balance:
        
            self.balance -= amount
            print(f"Withdraw: {amount}")
        else:
            print("not efficient")
    def get_balance(self):
        return self.balance
acc = BankAccount()
acc.deposit(500)
acc.withdraw(200)
print(f"Balance: {acc.get_balance}")

        



        