import json
students = [
    {"id":1,"name":"ALice","grade":"A"},
    {"id":2,"name":"Bob","grade":"B"}
]
with open("students.json","w") as f:
    json.dump(students,f,indent = 4)

with open("students.json","r") as f:
    data = json.load(f)
    print("Student record")
    for student in data:
        print(student)

