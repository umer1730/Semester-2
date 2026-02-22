import csv

employees = [{'name': 'John Smith', 'department': 'HR', 'birthday_month': 'July'},
{'name': 'Alice Johnson', 'department': 'IT', 'birthday_month': 'October'},
{'name': 'Bob Williams', 'department': 'Finance', 'birthday_month': 'January'}]

with open("employees.csv","r") as f:
    csv_reader = csv.DictReader(f)

    data_list = []
    for row in csv_reader:
        data_list.append(row)
for data in data_list:
    print(data)