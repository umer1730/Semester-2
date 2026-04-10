import csv

with open("D:\\Sem 2\\Sem 3\\CSV files\\stud.csv","r",newline ="",encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        # print(row)
        City = row[2]
        if City == "Lahore":
            print(row)
