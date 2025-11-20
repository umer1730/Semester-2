def get_student_info():
    """Collect name, roll number, and DOB. Determine number of courses from roll number"""
    name = input("Enter your name: ")
    roll_no = input("Enter roll number: ")
    dob_day = int(input("Enter birth day: "))

    # Extract last digit from roll number
    last_digit = ''.join([ch for ch in roll_no if ch.isdigit()])[-1:]  #joins all elements of a list into one continuous string without spaces or commas
    num_courses = int(last_digit) if last_digit else 0

    if num_courses == 0:
        print("Number of courses to enroll: 0 (Invalid or missing digit)")
    else:
        print(f"Number of courses to enroll: {num_courses}")

    return name, roll_no, dob_day, num_courses
get_student_info()