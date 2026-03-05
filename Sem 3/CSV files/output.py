import csv

def write_csv(filename,data,header = None):
    with open(filename,"w",newline = "",encoding="utf-8")as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(data)