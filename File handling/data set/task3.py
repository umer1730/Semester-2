import csv
high_score = []
with open("data.csv","r") as f:
    reader  =csv.reader(f)
    attend =0
    score = 0
    for row in reader:
        try:
            x = int(row)
            high_score.append(row)
        except:
            