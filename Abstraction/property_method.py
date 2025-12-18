class Circle:
    def __init__(self,radius):
        self._radius = radius
    @property
    def radius(self):
        print("Getting radius value")
        return self._radius
circle = Circle(5)
print(circle.radius)

print()
# class Circle:
#     def __init__(self,radius):
#         self._radius = radius
#     @property
#     def radius(self):
#         return self._radius
#     @radius.setter
#     def radius(self,value):
#         if value<0:
#             raise ValueError("Radius cannot be negative")
#         print(f"Setting radius to {value}")
#         self._radius = value
# circle = Circle(5)
# circle.radius = 10
# circle.radius = -5

print()
class Circle:
    def __init__(self,radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,value):
        self._radius = value
c = Circle(4)
print(c.radius)

class Circle:
    def __init__(self,radius):
        self._radius = radius
    def get_radius(self):
        return self._radius
    def set_radius(self,value):
        self._radius = value
    radius = property(get_radius,set_radius)

print()
class Bank:
    def __init__(self, balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")
b = Bank(100000)
print(b.balance)

b.deposit(1200)
b.withdraw(1000)
print(b.balance)
