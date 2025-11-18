class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount()
acc.deposit(1000)
print(acc.get_balance())

print()
class Person:
    def __hello(self):
        print(f"Hello {Person.__name}")
    def welcome(self):
        self.__hello()
p1 = Person()
p1.welcome()
p1.__hello()



