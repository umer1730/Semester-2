import csv

def load_data(filename):
    with open(filename,"r",newline = "",encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        return list(reader)

def compute_avg(data,col_index):
    total  = 0
    count = 0
    for  row in data:
        total += float(row[col_index])
        count += 1
    return total / count
data = load_data("stud.csv")
print(load_data("stud.csv"))
print(compute_avg(data,1))