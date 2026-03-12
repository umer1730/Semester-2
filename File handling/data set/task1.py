import csv
invalid_count=0
with open("data.csv","r",newline ="",encoding="utf-8") as f:
    reader =csv.reader(f)

    for row in reader:
        
        try:
            rows = int(row[2])
            
        except:
            invalid_count += 1
print(invalid_count)