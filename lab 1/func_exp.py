def greet():
    print("Hello")
greet()

print()
print("-----next-----")
def greet(name):
    print(f"Hello, {name}!")
greet("Ali")

print()
print("-----next-----")
def add(x,y):
    return x + y
result = add(5,3)
print(result)
# add(x=5,y=3)

print()
print("----------next-------")
def sum_all(*args):
    print(f"The arguments are a tuple: {args}")
    return sum(args)
print(sum_all(1,2,3,4))

print()
print("-----next------")
def print_info(**kwargs):
    print(f"the keyword arguments are a dictionary {kwargs}")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
print_info(name="Alice", age = 25)

print()
print("-----next------")
def add(x,y):
    return x + y
nums = [5,3]
print(add(*nums))
info = {'x': 10,'y': 20}
print(add(**info))

print()
print("-----next------")
def square(x):
    return x * x
res = square(5)
print(res)

print()
print("-----next------")
def get_data():
    name = "Alice"
    age = 25
    return name,age
user_name,user_age = get_data()
print(f"Name: {user_name}, Age: {user_age}")

print()
print("-----next-------")
def factorial(n):
    if n % 2 == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))

print()
print("-----next------")
import math
print(math.sqrt(16))

# or -------
print()
print("-----------")
from math import sqrt
print(sqrt(16))