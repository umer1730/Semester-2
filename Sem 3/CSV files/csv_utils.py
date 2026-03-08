import csv

def read_csv(filename):
    with open(filename,"r",newline = "",encoding="utf-8") as f:
        return list(csv.reader(f))
    
def write_csv(filename,data):
    with open(filename,"w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

print(read_csv("stud.csv"))
data = read_csv("stud.csv")
print(write_csv("stud.csv",data))