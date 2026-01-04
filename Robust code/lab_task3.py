class Bank(Exception):
    pass

class InsufficientFundsError(Bank):
    pass

class InvalidAccountError(Bank):
    pass

def withdraw(amount, balance):
    try:
        if amount > balance:
            raise InsufficientFundsError("Balance too low")
        balance -= amount
        print("Amount withdrawn successfully",e)
    except InsufficientFundsError as e:
        print(e)
        
def password(pin):
    try:
        if pin != 1234:
            raise InvalidAccountError("target does not exist")
        
        else:
            print("Access granted")
    except InvalidAccountError as e:
        print(e)

withdraw(800, 1000)
password(1234)
