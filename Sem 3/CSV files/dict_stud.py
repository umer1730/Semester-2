import csv

with open("D:\\Sem 2\\Sem 3\\CSV files\\stud.csv","r",newline="",encoding="utf-8") as f:
    # We use newline="" to prevent extra blank lines in the file.
    # we use encoding because when our data in other languages like chinese,arabic,french,german,emoji's etc...
    # Encoding  → Text ➜ Numbers
    # Decoding  → Numbers ➜ Text
    reader = csv.DictReader(f)

    for row in reader:
        #print(row)
        print(row["Name"], row["Age"])