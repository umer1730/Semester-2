class Car:
    def __init__(self):
        self.__speed = 0
    def accelerate(self,amount):
        if amount > 0:
            if self.__speed +amount <= 200:                
                self.__speed += amount
            else:
                self.__speed = 200
        else:    
            print("speed can not increase 200")
    def brake(self,amount):
        if amount <=0:
            if self.__speed - amount >=0:               
                self.__speed -= amount
            else:
                self.__speed=0
        else:   
            print("speed can not decreases below 0")
    def get_speed(self):
        return self.__speed
c = Car()
c.accelerate(50)
print("Speed: ",c.get_speed())

c.brake(50)
print("Speed: ",c.get_speed())

c.brake(10)
print("Speed: ",c.get_speed())

print()
print("-----6 next----")
class Temperature:
    def __init__(self,celcius):
        self.__celcius = celcius
    @property
    def temp(self):
        return self.__celcius
    @temp.setter
    def temp(self,celcius):
        if celcius >= -273.15:
            self.__celcius = celcius
        else:
            print("invalid temperature")
    def to_fahreheit(self):
        return (9/5*self.__celcius)+32
t = Temperature(25)
print("Temperature in celcius: ",t.temp)
print("Temperature in Fahrenheit: ",t.to_fahreheit())

t.temp = -300

t.temp = 33
print("Temperature in celcius: ",t.temp)
print("Temperature in Fahrenheit: ",t.to_fahreheit())

print()
print("---7next---")
class Book:
    def __init__(self,title,author,copies):
        self.__title  = title
        self.__author  = author
        self.__copies  = copies
    def borrow_book(self):
        if self.__copies > 0:
            self.__copies -= 1
            print(f"Book borrowed: {self.__copies}")
        else:
            print("not available")
    def return_book(self):
            self.__copies += 1
            print(f"Book returned: {self.__copies}")
    def get_copies(self):
        return self.__copies 
b = Book("Python","Guido",3)
b.borrow_book()
b.return_book()
print("Total copies: ",b.get_copies())

def add(x,y):
    return x+y
print(add(5,3))

print()
import pickle
class ObjectStore:
    def __init__(self):
        self.__objects = {}
    def add(self, obj_id, obj):
        self.__objects[obj_id] = obj
    def get_by_id(self, obj_id):
        return self.__objects.get(obj_id)
    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.__objects, f)
    def load(self, filename):
        with open(filename, "rb") as f:
            self.__objects = pickle.load(f)
store = ObjectStore()
store.add(1, "Book")
store.add(2, {"name": "Alice"})
store.save("db.pkl")
store.load("db.pkl")
print(store.get_by_id(2))
