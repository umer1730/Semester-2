import csv

total =0
count = 0

with open("D:\\Sem 2\\Sem 3\\CSV files\\plain.csv","r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        total += int(row[2])
        count += 1

average = total / count
print("Average Marks: ",average)