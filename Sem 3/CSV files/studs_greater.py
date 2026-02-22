import csv
with open("D:\\Sem 2\\Sem 3\\CSV files\\plain.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        marks = int(row[2])

        if marks > 80:
            print(row[0], marks)


        