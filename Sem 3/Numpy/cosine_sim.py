import numpy as np

A = np.array([[1,2],[3,4],[5,6]])
norm = np.linalg.norm(A,axis=1, keepdims=True)
A_norm = A / norm 

similarity = A_norm @ A_norm.T

print(similarity)