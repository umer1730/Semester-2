# try:
#     filename = "config.txt"
#     with open(filename,"r") as file:
#         data = file.read()
#     processed = process_data(data)
# except FileNotFoundError as e:
#     print(f"Error: {e}")
# except IOError as e:
#     print(f"error: {e}")

print()
Log_file = "log.txt"
print("---Overwriting test---")
with open(Log_file,"w") as f:
    f.write("Day3: New log started\n")

print("---appending---")
with open(Log_file,"a") as f:
    f.write("Day 4: Added new entry")

with open(Log_file,"r") as f:
    final_content = f.read()

print()
with open("data.txt","w") as f:
    f.write("This is data set")

with open("data.txt","r") as f:
    print(f.read())

import csv

FILE = "students.csv"

def add_student(name, gpa):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, gpa])
    print(f"Added: {name}, GPA: {gpa}")

def get_student(name):
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == name:
                student = {"name": row[0], "gpa": float(row[1])}
                print("Retrieved:", student)
                return
    print("Student not found")


# Test
add_student("Bob", 3.8)
get_student("Bob")

2
import json

FILE = "config.json"

def load_config():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_config(config):
    with open(FILE, "w") as f:
        json.dump(config, f, indent=4)

def update_config(key, value):
    config = load_config()
    config[key] = value
    save_config(config)
    print("Configuration updated")

def get_config(key):
    config = load_config()
    print(f"Current {key}: {config.get(key)}")


# Test
update_config("theme", "dark")
get_config("theme")

3
import pickle

FILE = "library.pkl"

class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("Titles:", self.books)

def save_object(obj):
    with open(FILE, "wb") as f:
        pickle.dump(obj, f)
    print(f"Saved {len(obj.books)} book objects")

def load_object():
    with open(FILE, "rb") as f:
        return pickle.load(f)


# Test
books = ["Python 101", "AI Fundamentals", "Data Science", "ML Basics"] * 4
library = Library(books[:15])

save_object(library)

loaded_library = load_object()
loaded_library.display_books()
