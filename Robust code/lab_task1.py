class Calculate(Exception):
    pass
try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    result = a / b
    print("Result: ",result)
except ZeroDivisionError:
    print("Can't divide zero")
except TypeError:
    print("Invalid input")


