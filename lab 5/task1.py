class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
s1 = Student("Rabia",90)
s2 = Student("Fatima",60)
del s2
del s1.name
print(s1.marks)
#print(s1.name) give error

print()
print("----next----")
class Book:
    def __init__(self, name):
        self.name = name
        print(f"Constructor: Book {self.name}")
    def __del__(self):
        print(f"Destructor: Book {self.name}")
b = Book("Poem")
del b
   
print()
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Person {self.name} is created")
    def __del__(self):
        print(f"Person {self.name} is destroyed")
p = Person("ALice",25)
del p
