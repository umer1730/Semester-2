class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Person {self.name} is created")
    def __del__(self):
        print(f"Person {self.age} is destroyed")
p = Person("Alice",25)
del p