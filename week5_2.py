class Student:
    name = "Ali"
    age = 20
student1 = Student()
student2 = Student()
student2.name = "Sara"
student2.gender = "Female"
print(student1.name,student1.age)
print(student2.name,student2.age,student2.gender)

Student.age = 22
print(student1.age,student2.age)


print()
print("-----next-----")
class Circle:
    def set_radius(self,r):
        self.radius = r
    def area(self):
        return 3.14*self.radius**2
c = Circle()
c.set_radius(5)
print(c.area())

print()
print("----next----")
class Student:
    name = "Unknown"
    course = "BS AI"

    def introduce(self):  
        return f"Hi, I'm {self.name} and I'm in course {self.course}"
student1 = Student()
student1.name = "Ali"

student2 = Student()
student2.name = "Sara"
print(student1.introduce())
print(student2.introduce())


print()
class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
s1 = Student("Ali",[99,98,97])
print(f"Hi {s1.name} your average score is {s1.average()}")