import csv
studednts = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},   
    {"name": "Charlie", "age": 19, "grade": "A"},
    {"name": "David", "age":21, "grade": "C"},
    {"name": "Eve", "age": 20, "grade": "B"}
]
with open("students.csv", mode = "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "grade"])
    writer.writeheader()
    writer.writerows(studednts)
print("Data written to students.csv successfully.")