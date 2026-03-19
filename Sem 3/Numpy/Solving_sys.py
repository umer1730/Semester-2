import numpy as np

A = np.array([[3, 1],
              [1, 2]])

b = np.array([9, 8])

solve = np.linalg.solve(A, b)

inv = np.linalg.inv(A) @ b
print(solve)
print()
print(inv)
