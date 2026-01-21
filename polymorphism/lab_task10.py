class Engine: 
    def start(self): 
        print("Engine starts") 
class Car: 
    def __init__(self): 
        self.engine = Engine()  # Composition: Car owns Engine 
    def start(self): 
        print("Car is starting...") 
        self.engine.start() 

car = Car() 
car.start() 

print()
class Aeroplane:
    Company = "AirSial"
    def __init__(self,name):
        self.name = name
    def display_info(self):
        print(f"Name: {self.name}")
class Employee(Aeroplane):
    def __init__(self,name,role,salary):
        self.name = name
        self.role =role
        self.__salary = salary
    def display_info(self):
        print(f"Name: {self.name} \nRole: {self.role} \nSalary: {self.__salary}")
class Passenger(Aeroplane):
    def __init__(self,name,seat_no):
        self.name = name
        self.seat_no = seat_no
    def display_info(self):
        print(f"Name: {self.name} \nSeat No: {self.seat_no}")

p = Passenger("ALi",12)
p.display_info()

e = Employee("Ahmed","SPO",100000)
e.display_info()

a = Aeroplane("asvchs")
a.display_info()