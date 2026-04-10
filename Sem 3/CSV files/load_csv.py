import csv
def read_csv(filename,has_header=True):
    with open(filename,"r",newline = "",encoding="utf-8")as f:
        reader = csv.reader(f)
        if has_header:
            header = next(reader)
            data = list(reader)
            return header,data
        
        return list(reader)
print(read_csv("D:\\Sem 2\\Sem 3\\CSV files\\stud.csv"))