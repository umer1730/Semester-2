import csv

highest = 0
top_student = ""

with open("D:\\Sem 2\\Sem 3\\CSV files\\plain.csv") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        marks = int(row[2])

        if marks > highest:
            highest = marks
            top_student = row[0]
        
print("Top Student: ", top_student)
print("Marks: ",highest)