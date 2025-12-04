class Person:
    def __init__(self,name,id_number):
        self.name = name
        self.id_number = id_number
    def display_info(self):
        print(f"Name: {self.name} ,ID: {self.id_number}")
class Student(Person):
    def __init__(self, name, id_number,major):
        super().__init__(name, id_number)
        self.major = major
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id_number}, Major: {self.major} ")
class Faculty(Person):
    def __init__(self, name, id_number,department):
        super().__init__(name, id_number)
        self.department = department
    def display_info(self):
#    def assign_course(self,course_name):
        print(f"Name: {self.name},ID: {self.id_number},Department: {self.department}")
    def assign_course(course_name):
        print(f"Course {course_name} assigned to")
p = Person("Ahmed",222)
p.display_info()

s = Student("Uzair",12,"AI")
s.display_info()
f = Faculty("Ali",32,"Electrical")
f.display_info()
f.assign_course()        