import random
def login_system(password="oop123",max_attempts=3):
    for attempt in range(max_attempts):
        entered=input("Entered password:")
        if entered==password:
            print("Access generated!")
            return True
        else:
            print("Not Access!")
    print("To many attemots!Access denied")
    return False
login_system()

def get_student_info():
    name=input("enter your name:")
    rollnum=input("enter rollnumber:")
    dob=input("enter your DOB:")
    last_digit=rollnum[-1]
    if last_digit.isdigit():
        num_courses=int(last_digit)
    else:
        num_courses=5
    if num_courses==0:
        num_courses=5
    print(f"Number of courses to enroll:{num_courses}")  
    return name,rollnum,dob,num_courses   
get_student_info()

def enroll_courses(num_courses):
    all_courses=["python","oop","DBMS","AI","DSA","CYB","EE","CS","SE"]
    courses=all_courses[:num_courses]
    print("Courses:",courses)
    return courses
enroll_courses(5)

def generate_marks(num_courses):
    marks=[random.randint(50,100) for i in range(num_courses)]
    print(marks)
    return marks
generate_marks(5)