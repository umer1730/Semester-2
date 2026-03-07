import csv

with open("sales.csv","r",newline="",encoding="utf-8") as f:
    reader = csv.reader(f)

    header  =next(reader)
    for row in reader:
        print(row)