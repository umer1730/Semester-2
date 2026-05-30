import numpy as np

A = np.array([[1,5,3,2],[9,7,8,6]])
k = 2

indices = np.argsort(A,axis = 1)[:, -k:]
topk = np.take_along_axis(A,indices ,axis=1)

print(topk)