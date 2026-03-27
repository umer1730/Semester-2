import numpy as np

A = np.arange(1,17).reshape(4,4)
k = 2

reshaped = A.reshape(A.shape[0]//k,k, A.shape[1]//k,k)

result = reshaped.sum(axis = (1,3))
print(result)