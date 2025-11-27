def generate_marks(dob_day, num_courses):
    """Generate reproducible marks (50-100) without using random.seed()."""
    available_courses = ['Python', 'OOP', 'DBMS', 'AI', 'DSA']
    print("Generated marks:")
    
    marks = []
    for i in range(num_courses):
        # Use hash to create a pseudo-random but repeatable mark
        value = (hash((dob_day, i)) % 51) + 50
        marks.append(value)
        course_name = available_courses[i % len(available_courses)]
        print(f"{course_name}: {value}")

    return marks

generate_marks(15, 5)
