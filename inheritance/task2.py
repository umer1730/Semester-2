class Animal:
    def speak(self):
        print("Aniaml speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.speak()
d.bark()

print()
class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("Car stopped")
class Toyota(Car):
    def __init__(self,model):
        self.model = model
class Toyota_GLI(Toyota):
    def __init__(self,type):
        self.type = type
c1 = Toyota_GLI("auto")
c1.model = "2025"
print(c1.type)
print(c1.model)
c1.start()
        