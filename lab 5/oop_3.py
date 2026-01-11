class Database:
    def __init__(self,name):
        self.name = name
        print(f"Connection to {self.name}")
    def __del__(self):
        print(f"Connection closed")
db =  Database("mydb")
del db
        
print()
class BankAccount:
    def __init__(self, initial_balance, pin):
        self.__balance = initial_balance 
        self.__pin = pin                  
        self.transaction_count = 0
    def __verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount, pin):
        if self.transaction_count >= 3:
            return "Account closed."
        
        if self.__verify_pin(pin):
            self.__balance += amount
            self.transaction_count += 1
            return f"Deposited {amount}. Balance: {self.__balance}"
        return "Invalid PIN"

    def withdraw(self, amount, pin):
        if self.transaction_count >= 3:
            return "Account closed."
            
        if self.__verify_pin(pin) and amount <= self.__balance:
            self.__balance -= amount
            self.transaction_count += 1
            return f"Withdrew {amount}. Balance: {self.__balance}"
        return "Invalid PIN or insufficient funds"
b = BankAccount(1000,1234)
print(b.deposit(200,1234))
print(b.withdraw(200,1234))