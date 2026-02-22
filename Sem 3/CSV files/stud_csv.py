import csv

with open("D:\\Sem 2\\Sem 3\\CSV files\\stud.csv","r") as f:
    csv_reader = csv.reader(f)

    next(csv_reader) #skip first line
    for row in csv_reader:
       # print(row)

        print()
        print(row[0]) #print names only
