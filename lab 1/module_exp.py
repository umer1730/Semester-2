import math
print(math.sqrt(16))

# or -------
print()
print("-----------")
from math import sqrt
print(sqrt(16))

print()
print("----next----")
import numpy as np
import pandas as pd
from math import sqrt as square_root
print(np.array([1,2,3]))
print(square_root(25))

print()
print("-----next----")
def add(x,y):
    return x + y
add_lambda = lambda x,y: x + y
print(add_lambda(2,3))

print()
print("-----next------")
add = lambda x, y:x + y
print(add(5,3))

print()
print("----next----")
is_even = lambda x: x % 2 ==0
print(is_even(10))
print(is_even(7))

print()
print("---next----")
high_scores = [('Alice',150),('Bob',90),('Charlie',200)]
sorted_scores = sorted(high_scores, key=lambda item: item[1])
print(sorted_scores)