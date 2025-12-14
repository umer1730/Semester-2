#A class method is a method that works with the class itself, not with individual objects.
#It can access and modify class variables.
class Student:
    school = "UET"
    count = 0
    def __init__(self,name):
        self.name =  name
        Student.count += 1
    @classmethod
    def get_school_info(cls):
        return f"School: {cls.school} \nStudents: {cls.count}"
    @classmethod
    def reset_count_to(cls,x):
        if x > 0:
            Student.count = x
stu1 = Student("Ali")
print(stu1.count)
stu2 = Student("Sara")
print(stu2.count) 
print(Student.get_school_info())
student = Student.reset_count_to(20)
print(stu1.count)
print(Student.get_school_info())

print()
class Temperature:
    Freezing_point = 0
    def __init__(self,celcius):
        self.celcius = celcius
    def to_fahrenheit(self):
        return (self.celcius*9/5)+32
    @classmethod
    def from_fahrenheit(cls,fahrenheit):
        celcius = (fahrenheit-32)*5/9
        return cls(celcius)
temp_c = Temperature(25)
print(f"Standard creation: {temp_c.celcius:.2f}C")
temp_f = Temperature.from_fahrenheit(68)
print(f"ALternative creation: {temp_f.celcius:.2f}C")
print(f"Check conversion: {temp_f.to_fahrenheit():.2f}F")   

print()
class Greeks:
    course = "Python"                 
    list_of_instance = []             

    def __init__(self, name):          
        self.name = name
        Greeks.list_of_instance.append(self)

    @classmethod
    def get_course(cls):               
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):        
        return f"Number of instances: {len(cls.list_of_instance)}"

    @staticmethod
    def welcome_message():             
        return "Welcome to Geeks for Geeks"

# creating objects
g1 = Greeks("Ali")
g2 = Greeks("Bob")

print(Greeks.get_course())
print(Greeks.get_instance_count())
print(Greeks.welcome_message())

print()
class Student:
    name = "Ali"
    def print_name(self):
        print("The name is: ",self.name)
Student.print_name = classmethod(Student.print_name)
Student.print_name()

print()
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
date = Date.from_string('2023-07-16')
print(date.year, date.month, date.day)

print()
from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def from_FathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def from_BirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
    def display(self):
        print(self.name + "'s age is: " + str(self.age))
class Man(Person):
    sex = 'Female'
man = Man.from_BirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.from_FathersAge('John', 1965, 20)
print(isinstance(man1, Man))

print()
from datetime import date
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year - year)
    
    @staticmethod
    def adult(age):
        return age >= 18
    
person_1 = Person("Ali",12)
person_2 = Person.fromBirthYear("Saad",9)
print(f"Person 1 age: {person_1.age}")
print(f"Person 2 age: {person_2.age}")

print()
class Student:
    count  = 0
    total_cgpa = 0
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
        Student.count = 1
        Student.total_cgpa = gpa
    
    def get_info(self):
        print(f"{self.name} \n{self.age} \n{self.gpa}")

    @classmethod
    def get_count(cls):
        return f"Total no of student's count: {cls.count}"
    
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_cgpa / cls.count}"
student_1 = Student("Saad",9,3.2)
student_2 = Student("Saim",10,3.3)
student_3 = Student("Saeed",11,4.0)
student_4 = Student("Salah",12,3.5)
print(Student.get_count())
print(Student.average_gpa())