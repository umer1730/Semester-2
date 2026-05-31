import numpy as np
A = np.zeros((1000,1000))

rows = np.random.randint(0,1000,10)
cols = np.random.randint(0,1000,10)

A[rows, cols] = np.random.randint(1,100,10)
print(A)