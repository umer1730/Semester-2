import random

def pick_students(students, k, seed):
    random.seed(seed)
    return random.sample(students,k)

students = ["Ali","Sara","Haris","Zara","Usman","Noor"]
print(pick_students(students,3,10))