class Session:
    active_sessions =0
    def __init__(self):
        Session.active_sessions +=1
    def __del__(self):
        Session.active_sessions -= 1
s1 = Session()
s2 = Session()
print(f"Active sessions: {Session.active_sessions}")
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80:
            return 'A'
        elif self.marks >= 60:
            return 'B'
        else:
            return 'C'
s1 = Student('Ayesha', 7, 85)
print(s1.get_grade())    
