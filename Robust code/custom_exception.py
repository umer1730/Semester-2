class PaymentError(Exception):
    pass
class InsufficientFundsError(PaymentError):
    pass
class InvalidAmountError(PaymentError):
    pass
class PaymentGatewayError(PaymentError):
    pass
def process_order(amount,user_balance):
    if amount > user_balance:
        raise InsufficientFundsError(f"Need ${amount - user_balance} more")
    if amount <= 0:
        raise InvalidAmountError(f"${amount} is invalid")
process_order(100,90)
print()
class AgeError(Exception):
    pass
def check_age(age):
    if age < 18:
        raise AgeError("Age ust be 18 or above")
    return "Access granted"
try:
    print(check_age(15))
except AgeError as e:
    print(e)
print()
class BooksNotAvailable(Exception):
    pass
class Library:
    def __init__(self):
        self.books = {"Python": 1}
    def borrow(self,book):
        if self.books.get(book,0) == 0:
           raise BooksNotAvailable("Books not available")
        self.books[book] -= 1
        print("book borrowed")
lib = Library()
try:
   lib.borrow("Python")
   lib.borrow("Python")
except BooksNotAvailable as e:
   print(e)

print()
class SalaryReductionError(Exception):
    pass
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary    
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,value):
        if value < self.__salary:
            raise SalaryReductionError(f"Cannot reduce salary from {self.__salary} to {value}!")
        self.__salary = value
        print(f"Salary updated to {self.__salary}")
emp = Employee("ALi",10000)
try:
    emp.salary = 1200
except SalaryReductionError as e:
    print(f"Alert: {e}")