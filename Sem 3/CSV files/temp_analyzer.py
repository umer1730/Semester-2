import csv

def load_data(filename):
    data = []
    with open(filename,newline ="") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            data.append(int(row[1]))
    return data

def get_average_temp(data):
    return sum(data) / len(data)

def get_max_temp(data):
    return max(data)

def print_summary(avg,max_temp):
    print("Average temp: ",avg)
    print("Max Temp: ",max_temp)

def main():
    data = load_data("D:\\Sem 2\\Sem 3\\CSV files\\temps.csv")
    avg = get_average_temp(data)
    mx = get_max_temp(data)
    print_summary(avg,mx)

if __name__ == "__main__":
    main()