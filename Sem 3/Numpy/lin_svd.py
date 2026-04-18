import numpy as np
A = np.array([[1,2,3],[2,4,6],[1,1,1]])

U,S,V = np.linalg.svd(A)

rank = np.sum(S > 1e-10)

print(rank)