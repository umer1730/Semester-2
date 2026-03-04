import csv

with open("stud.csv","r",newline ="",encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)