import csv

with open("dataset.csv","r",newline="",encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)
    for row in reader:
        salary = int(row[3])
        name = row[1]
        if name == "Alice":
            print(f"{name} earns ${salary}")

   