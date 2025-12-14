print()
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
        
    
