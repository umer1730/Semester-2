student_name = "Ali"
student_id = "2025-SAI-123"
courses = ["Python", "OOP", "DBMS", "AI", "DSA"]
marks = [86, 80, 92, 67, 75]  # initial marks
# function to add or update mark
def add_or_update_mark():
    course = input("Enter course name: ").strip()
    if course in courses:
        new_mark = float(input("Enter new mark: "))
        index = courses.index(course)
        marks[index] = new_mark
        print(f"Mark updated for {course}.")
    else:
        print("Course not found.")

# functions
def show_summary():
    print(f"\nStudent: {student_name} ({student_id})")
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

# LMS menu loop
while True:
    print("\n----- LMS MENU -----")
    print("1. Add/Update Mark")
    print("2. Show Summary")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_or_update_mark()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        print("Exiting LMS... Goodbye!")  # then exit lms
        break
    else:
        print("Invalid option. Try again.")
