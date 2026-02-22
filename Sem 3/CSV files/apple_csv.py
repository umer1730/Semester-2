import csv
filename = "apple.csv"
fields = []
rows = []

with open(filename,"r") as f:
    csv_reader =csv.reader(f)

    fields =next(csv_reader)
    for row in csv_reader:
        rows.append(row)

    print("Total no. of rows: %d" % csv_reader.line_num)
    