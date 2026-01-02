with open("demofile.txt","w") as f:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    place = input("Enter place: ")
    do = input("Enter work: ")

    f.write(f"What is your name: {name}\n")
    f.write(f"What is your age: {age}\n")
    f.write(f"Where do you from: {place}\n")
    f.write(f"What are you doing: {do}")


import csv

FILE_NAME = "students.csv"

def add_student(name, gpa):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, gpa])
    print(f"Added: {name}, GPA: {gpa}")

def get_student(name):
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                student = {"name": row[0], "gpa": float(row[1])}
                print(f"Retrieved: {student}")
                return student
    return None

# Test
add_student("Bob", 3.8)
get_student("Bob")

2
import json

CONFIG_FILE = "config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def update_config(key, value):
    config = load_config()
    config[key] = value
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file)
    print(f"Configuration updated Current {key}: {value}")

def get_config(key):
    config = load_config()
    return config.get(key)

# Test
update_config("theme", "dark")
print("Current theme:", get_config("theme"))

3
import pickle

FILE_NAME = "library.pkl"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

    def display_books(self):
        print("Book Titles:", self.books)

def save_object(obj):
    with open(FILE_NAME, "wb") as file:
        pickle.dump(obj, file)
    print(f"Saved {len(obj.books)} book objects")

def load_object():
    with open(FILE_NAME, "rb") as file:
        return pickle.load(file)

# Create library object
library = Library()
books = [
    "Python 101", "AI Fundamentals", "Data Science", "ML Basics",
    "Deep Learning", "Algorithms", "Databases", "Networking",
    "OS Concepts", "Cyber Security", "Web Dev", "Cloud Computing",
    "Big Data", "IoT", "Robotics"
]

for book in books:
    library.add_book(book)

# Test
save_object(library)
loaded_library = load_object()
loaded_library.display_books()

