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