import csv 

with open("data.csv","r",newline ="",encoding = "utf-8") as f:
    reader =  csv.reader(f)
    high=0
    medium=0
    low=0
    header = next(reader)
    for row in reader:
        try:
            x = int(row)
            if row[2] >= 80:
                high +=1
            elif row[2] >=50 and row[2] <=79:
                medium +=1
            else:
                low += 1
        except:
            invalid +=1
        