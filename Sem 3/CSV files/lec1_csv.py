import csv

with open("stud.csv","r",newline = "",encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)
    print(f"Processing: {header}")
    for row in reader:
        Name = row[0]
        Age = int(row[1])
        if Age > 20:
            print(Name)
    # for row in reader:
    #     print(row)