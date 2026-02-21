def enroll_courses(num_courses):
    """Auto-enroll N courses from predefined list"""
    available_courses = ['Python', 'OOP', 'DBMS', 'AI', 'DSA']
    print(f"Auto-enrolling {num_courses} courses...")

    courses = available_courses[:num_courses]
    print(f"Courses: {courses}")
    return courses

enroll_courses(5)

print()
class Student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.courses = enroll_courses(5)
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Enrolled Courses: {self.courses}")
student =Student()
student.display_info()

        