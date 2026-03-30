import numpy as np

A = np.arange(1,31)

A[(A % 3 == 0) & (A % 5 == 0)] = -15
A[(A % 3 == 0) & (A % 5 != 0)] = -3
A[(A % 5 == 0) & (A % 3 != 0)] = -5

print(A)