import numpy as np
A = np.array([[1,2,3],[5,6,7]])

row_sum = A.sum(axis =1,keepdims=True)
normalized = A / row_sum

print(normalized)