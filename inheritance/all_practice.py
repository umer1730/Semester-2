class Person:
    def __init__(self,name,id_no):
        self.name = name
        self.id_no = id_no
    def display_info(self):
        return f"Name: {self.name} \nID: {self.id_no}"
class Student(Person):
    def __init__(self,name,id_no,major):
        super().__init__(name,id_no)
        self.major = major
    def display_info(self):
        return f"Name: {self.name}\nID: {self.id_no} \nMajor: {self.major}"
class Faculty(Person):
    def __init__(self,name,id_no,department):
        super().__init__(name,id_no)
        self.department = department
    def display_info(self):
        return f"Name: {self.name} \nID: {self.id_no} \nDepartment: {self.department}"
    def assign_course(course_name):
        return f"{course_name} assigned to"
p = Person("Ali",22)
print(p.display_info())
s = Student("Arslan",134,"AI")
print(s.display_info())
f = Faculty("adeem",678,"AI")
print(f.display_info())
print(f.assign_course())
