class Student:
    name = "Alice"
    age = 23
print(Student.name)
print(Student.age)


print()
print("-------next-------")
class Pet:
    name = "Dog"
print(Pet.name)


print()
print("-----next------")
class Student:
    name = "Ali"
    age = 23
student_1 = Student()
student_2 = Student()
student_2.name = "Sara"
print(student_1.name)
print(student_2.name)
print(student_1.age == student_2.age)
 

print()
print("----next-----")
class Book:
    name = "Python"
    website = "W3schools"
book_1 = Book() 
book_2 = Book()
book_2.name = "Java"
print(book_1.name)
print(book_2.name)
print(book_1.website == book_2.website)


print()
print("-----next------")
class Vehicle:
    wheels = 4
    color = None
car_1 = Vehicle()
car_1.color = "red"
car_2 = Vehicle()
car_2.color = "black"
print(car_1.color, car_1.wheels)    
print(car_2.color, car_2.wheels)    