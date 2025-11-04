class Car:
    wheels = 4
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Wheels: {Car.wheels}")
    def change_color(self,new_color):
        self.color = new_color
        print(f"Color changed to {self.color}")
car1 = Car("Toyota","Red")
car2 = Car("Honda","yellow")
print(car1.brand)
print(car2.brand)
print(Car.wheels)
car1.display_info()
car2.display_info()

car1.change_color("Black")
car1.display_info()


print()
print("----next example----")
class Student:
    university_name = "U.E.T, Lahore"
    def __init__(self,name,age,grade,department):
        self.name = name
        self.age = age
        self.grade = grade
        self.department = department
    def display_info(self):
        print(f"Name: {self.name} \nAge: {self.age} \nGrade: {self.grade} \nDepartment: {self.department} \nUniversity Name: {Student.university_name}")
s1 = Student("Ali",20,"A","Artificcial Intelligence")
s1.display_info()


print()
print("-----next-----")
print()
class Employee:
    company = "Arbisoft"
    def __init__(self,name,age,designation,salary,position):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary
        self.position = position
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")
        print(f"Position: {self.position}")
        print(f"Company: {Employee.company}")
employee_details = Employee("Ali",27,"Software Engineer",150000,"Senior")
employee_details.display_info()