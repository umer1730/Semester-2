import csv

with open("D:\\Sem 2\\Sem 3\\CSV files\\dataset.csv","r",newline="",encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)
    for row in reader:
        salary = int(row[3])
        name = row[1]
        if name == "Alice":
            print(f"{name} earns ${salary}")

print()
with open("D:\\Sem 2\\Sem 3\\CSV files\\dataset.csv","r",newline="",encoding="utf-8") as infile:
        reader = csv.reader(infile)

        header = next(reader)                
        for row in reader:
            salary = int(row[3])   # assuming salary is in column 4
            if salary > 75000:
                print(row)


print()
import csv


dept_data = {} 

with open("D:\\Sem 2\\Sem 3\\CSV files\\dataset.csv", "r", newline="", encoding="utf-8") as f:
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
            

