import csv
import random

def read_csv(filename, has_header=True):
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        if has_header:
            header = next(reader)
            data = list(reader)
            return header, data
        return list(reader)

def filter_by_value(data, col_index, threshold):
    return [row for row in data if float(row[col_index]) > threshold]

def compute_average(data, col_index):
    values = [float(row[col_index]) for row in data]
    return sum(values) / len(values)

def random_sample(data,fraction,seed=None):
    if seed is not None:
        random.seed(seed)
    n = int(len(data) * fraction)
    return random.sample(data,n)

header, data = read_csv("stud.csv")

print("Age > 20:")
print(filter_by_value(data, 1, 20))

print("Average Age:")
print(compute_average(data, 1))