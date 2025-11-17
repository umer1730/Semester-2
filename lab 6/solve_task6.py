class BankAccount:
    def __init__(self,balance,pin):
        self.__balance = balance
        self.__pin = pin
        self.__transactions = 0
        self.__closed = False
    def __verify_pin(self,pin):
        if self.__closed:
            print(f"Account is closed.No further transactions allowed")
            return False
        if pin != self.__pin:
            print("Incorrect pin")
            return False
        return True
    def deposit(self,amount,pin):
        if self.__verify_pin(pin):
            if amount > self.__balance:
                print("Insufficient Balance.Transaction cancelled")
            else:
                self.__balance -= amount
                print(f"Withdraw ${amount}. New balance: ${self.__balance}")
                self.__transactions +=1
                self.__check_close()
    def withdraw(self,amount,pin):
        if self.__verify_pin(pin):
            if amount > self.__balance:
                print("Insufficient balance. transaction cancelled")
            else:
                self.__balance -= amount
                print(f"Withdraw ${amount}. New balance: ${self.__balance}")
                self.__transactions +=1
                self.__check_close()
    def check_balance(self,pin):
        if self.__verify_pin(pin):
            print(f"Current balance: ${self.__balance}")
            self.__transactions += 1
            self.__check_close()
    def __check_close(self):
        if self.__transactions>= 3:
            self.__closed = True
            print(f"\nAccount closed. Final BalanceL ${self.__balance}") 
account = BankAccount(1000,1234)
account.deposit(500,1234)
account.withdraw(200,1234)
account.check_balance(1234)
account.deposit(300,1234)

