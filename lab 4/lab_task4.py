class Student:
    name="Rabia"
s1 = Student()
print(s1)
print(s1.name)

#craete class
class Dress:
    color = "blue"
    length = "long"
    size = ['s','m','l']
d1 = Dress()
print(d1.color)
print(d1.length)
print(d1.size)
print(d1.size[2])

#constructor or init fun
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in database")
s1 = Student("Rabia",33)
print(s1.name,s1.marks)
# second object
s2 = Student("Fatima",99)
print(s2.name,s2.marks)

#create class
class Student:
    college = "UET"
    grade = "A"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in databse")
s1 = Student("Rabia",100)
print(f"Information of student 1: {s1.name}, {s1.marks}, {s1.college}, {s1.grade}")
s2 = Student("Fatima",23)
print(f"Information of student 2: {s2.name}, {s2.marks}, {s2.college}, {s2.grade}")

class BankAccount:
    def __init__(self,deposit,withdraw):
        self.deposit = deposit
        self.withdraw = withdraw
    def balance(self):
        print(f"Balance: {self.deposit-self.withdraw}")
acc = BankAccount(500,200)
acc.balance()