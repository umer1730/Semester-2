import statistics

def student_result(name, *marks, grade='Pending'):
    avg = statistics.mean(marks)
    assign_grade = lambda a: (
        'A+' if a >= 90 else
        'A' if a >= 80 else
        'B' if a>= 70 else
        'C' if a>=60 else
        'D' if a>=50 else
        'F'
    )

    grade = assign_grade(avg)
    print(f"Student Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"{name}'s average marks is {avg} and he got {grade} grade")
    return name, marks, avg, grade
student_result("Ali", 85,90,80,75,90,98)

print()
print("-----------------------")
numbers = [1,2,3]
squares = []
for n in numbers:
    squares.append(n**2)
print(squares)

print()
print("-------------")
fruits = ["apple",'banana','orange','pineapple']
newlist = []
for x in fruits:
    if x != 'apple':
        newlist.append(x)
print(newlist)