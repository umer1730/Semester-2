class Equal:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def __eq__(self, other):
        return self.rollno == other.rollno
    def __str__(self):
        return f"Students are equal Students object by roll number"
v1 = Equal("Ali", 24)
v2 = Equal("Arslan", 24)
print(v1)
