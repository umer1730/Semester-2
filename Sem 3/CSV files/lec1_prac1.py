import csv

with open("dataset.csv","r",newline="",encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)
    for row in reader:
        salary = int(row[3])
        name = row[1]
        if name == "Alice":
            print(f"{name} earns ${salary}")

print()
with open("dataset.csv","r",newline="",encoding="utf-8") as infile:
    with open("high_earners.csv","w",newline="",encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)         
        writer.writerow(header)        

        for row in reader:
            salary = int(row[3])       
            if salary > 70000:
                writer.writerow(row)


print()
import csv


dept_data = {} 

with open("dataset.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)  
    
    for row in reader:
        dept = row["department"]
        salary = int(row["salary"])
        
        if dept not in dept_data:
            dept_data[dept] = [0, 0]  
        
        dept_data[dept][0] += salary  
        dept_data[dept][1] += 1      

for dept, (total_salary, count) in dept_data.items():
    avg_salary = total_salary / count
    print(f"Average salary in {dept}: ${avg_salary:.2f}")
            

