import pickle
student = {
    "id": 101,
    "Name": "Alice",
    "marks":89
}
with open("student.data","wb") as f:
    pickle.dump(student,f)

with open("student.data","rb") as f:
    data = pickle.load(f)
    print(data)
