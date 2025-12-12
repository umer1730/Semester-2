class Person:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def display(self):
        print(f"Name: {self.name} \nAge: {self.age}")
class Student(Person):
    def __init__(self,name,age,student_id,grade):
        super().__init__(name,age)
        self.student_id = student_id
        self.grade = grade
    def display(self):
        super().display()
        print(f"Student ID: {self.student_id} \nGrade: {self.grade}")
class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary
    def display(self):
        super().display()
        print(f"Subject: {self.subject} \nSalary: {self.salary}")
class Staff(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department = department
    def display(self):
        super().display()
        print(f"Department: {self.department}")
student_1 = Student("Alice",16,"AI26","A")
teacher_1 = Teacher("Alice",26,"OOP",50000)
staff_1 = Staff("Alice",35,"AI")
print("\n---Student Info---")
student_1.display()

print("\n---Teacher Info---")
teacher_1.display()

print("\n---Staff Info---")
staff_1.display()