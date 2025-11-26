def enroll_courses(num_courses):
    """Auto-enroll N courses from predefined list"""
    available_courses = ['Python', 'OOP', 'DBMS', 'AI', 'DSA']
    print(f"Auto-enrolling {num_courses} courses...")

    courses = available_courses[:num_courses]
    print(f"Courses: {courses}")
    return courses

enroll_courses(5)