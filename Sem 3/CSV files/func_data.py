import csv

def load_data(file):
    with open(file,"r",newline="",encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        return header,list(reader)
    
def filter_data(data, col,threshold):
    return [row for row in data if int(row[col]) > threshold]

def save_data(file,header,data):
    with open(file,"w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

def main():
    header,data = load_data("sales.csv")
    filtered_data = filter_data(data,2,2)
    save_data("filtered.csv",header,filtered_data)

if __name__ == "__main__":
    main()
