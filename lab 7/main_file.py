from lms_utils import login_system, get_student_info, enroll_courses, generate_marks

class Student:
    def __init__(self,name,rollnum,dob,courses):
        self.name=name
        self.rollnum=rollnum
        self.dob=dob
        self.dob=dob
        self.courses=courses
        self.marks=[]
    def add_marks(self,marks):
        self.marks=marks
    def show_summary(self):
        print(f"\nStudent:{self.name}({self.rollnum})") 
        print(f"Courses:{self.courses}")
        print(f"Marks:{self.marks}")
        if self.marks:
            avg = sum(self.marks) / len(self.marks)
            print(f"Average: {avg}")
            if avg >= 80:
                performance = "Excellent"
            elif avg >= 70:
                performance = "Good"
            elif avg >= 60:
                performance = "Average"
            else:
                performance = "Poor"
            print(f"Performance: {performance}")
if not login_system():
        exit()

name, roll_no, dob_day, num_courses = get_student_info()
courses = enroll_courses(num_courses)
student = Student(name, roll_no, dob_day, courses)
marks = generate_marks(len(courses))

print("\nGenerated marks:")
for course, mark in zip(courses, marks):
    print(f"{course}: {mark}")

student.add_marks(marks)
student.show_summary()