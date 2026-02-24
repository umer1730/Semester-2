import csv 
with open("D:\\Sem 2\\Sem 3\\CSV files\\university_records.csv","r") as f:
    csv_reader = csv.reader(f)
    
    # next(csv_reader)
    for line in csv_reader:
        #print(line)
        
        print(line)


