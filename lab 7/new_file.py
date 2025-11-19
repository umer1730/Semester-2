from lms_utils import login_system, get_student_info, enroll_courses, generate_marks

def show_summary(name, roll_no, courses, marks):
    """Display student summary and performance"""
    print(f"\nStudent: {name} ({roll_no})")
    print(f"Courses: {courses}")
    print(f"Marks: {marks}")
    avg = sum(marks) / len(marks)
    print(f"Average: {avg:.1f}")

    if avg >= 85:
        performance = "Excellent"
    elif avg >= 70:
        performance = "Good"
    elif avg >= 50:
        performance = "Average"
    else:
        performance = "Poor"

    print(f"Performance: {performance}")


def main():
    print("Welcome to the Mini Learning Management System\n")
    if not login_system():
        return

    name, roll_no, dob_day, num_courses = get_student_info()
# Enroll courses
    courses = enroll_courses(num_courses)

    marks = generate_marks(dob_day, num_courses)

    # Step 5: Menu
    while True:
        print("----- LMS MENU -----")
        print("1. Add/Update Mark")
        print("2. Show Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            course = input("Enter course name: ").strip()   #strip is used to break the string
            if course in courses:
                new_mark = float(input("Enter new mark: "))
                index = courses.index(course)       # index is used to find the position of item in the list
                marks[index] = new_mark
                print(f"Mark updated for {course}.")
            else:
                print("Course not found.")

        elif choice == "2":
            show_summary(name, roll_no, courses, marks)

        elif choice == "3":
            print("Exiting LMS... Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":  
    main()
