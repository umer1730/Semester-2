import math as m
from math import sqrt
# Using imported module and alias
print("Value of Pi:", m.pi)
print("Square root of 16:", sqrt(16)) # Direct import us
# Lambda example
area = lambda l, w: l * w
print("Area of rectangle (5x3):", area(5, 3))

# Lambda example
cube = lambda x: x * x * x
print("Cube of 5:", cube(5))

print()
print("--------next------")

import statistics as stats
from math import sqrt
def analyze_data(*data, round_to=2):
    mean = stats.mean(data)
    stdev = stats.stdev(data)
    root = sqrt(mean)
    return round(mean, round_to), round(stdev, round_to), round(root, round_to)
# Example call
mean_val, stdev_val, root_val = analyze_data(10, 20, 30, 40, 50)
print(f"Mean: {mean_val}, Std Dev: {stdev_val}, √Mean: {root_val}")