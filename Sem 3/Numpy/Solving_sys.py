import numpy as np

A = np.array([[3, 1],
              [1, 2]])

b = np.array([9, 8])

solution = np.linalg.solve(A, b)
print(solution)
