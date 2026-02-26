import csv

with open("D:\\Sem 2\\Sem 3\\CSV files\\stud.csv","r") as f:
    csv_reader = csv.reader(f)

    next(csv_reader) #skip first line
    for row in csv_reader:
       # print(row)

        print()
        print(row[0]) #print names only

        age = int(row[1])
        print(age)

    






# import csv

# with open("new_students.csv", "w", newline="") as file:
#     writer = csv.writer(file)
    
#     writer.writerow(["Name", "Age", "City"])
#     writer.writerow(["Usman", 21, "Lahore",6.0])
#     writer.writerow(["Ali", 22, "Karachi",5.2])