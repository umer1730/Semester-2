from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def refill(self):
        pass
class Car(Vehicle):
    def move(self):
        print("Car move on land with four wheels")
    def refill(self):
        print("4 wheel car refills 50L fuels")
class Truck(Vehicle):
    def move(self):
        print("Truck move on land with six wheels")
    def refill(self):
        print("6 wheels truck refills 100L fuels")
class Plane(Vehicle):
    def move(self):
        print("Plane move in air")
    def refill(self):
        print("plan refills 500L fuels")
