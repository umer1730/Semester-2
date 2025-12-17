#Implicit abstraction happens automatically when we use built-in features of a language.

class BankAccount:
    def __init__(self,initial_balance):
        self._balance =  initial_balance
    def deposit(self,amount):
        self._balance += amount
    def get_balance(self):
        return self._balance
b = BankAccount(0)  
b.deposit(222)
print(b.get_balance())

print()
class Student:
    def show(self):
        print("Student info")
s = Student()
s.show()