import csv

with open("D:\Sem 2\Sem 3\CSV files\plain.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if int(row["Marks"]) >= 90:
            print(row["Name"], "got A+ grade")