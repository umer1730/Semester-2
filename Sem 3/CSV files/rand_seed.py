import random
import csv

random.seed(4)

with open("plain.csv","r",newline="",encoding="utf-8") as f:
    rows = list(csv.reader(f))

sample = random.sample(rows,2)
print(sample)