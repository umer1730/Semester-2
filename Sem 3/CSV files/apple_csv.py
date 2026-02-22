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

print("Fiels names are: "+",".join(fields))

print("\nFirst five rows are:\n")
for row in rows[:5]:
    for col in row:
        print("%10s"% col,end=" ")
    print('\n')
    