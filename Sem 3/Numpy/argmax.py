import numpy as np

A = np.array([
    [3, 8, 5, 2],
    [7, 1, 6, 4],
    [9, 3, 5, 11]
])

mask = (A % 2 == 0)
A_masked = np.where(mask, A, -np.inf)

indices = np.argmax(A_masked, axis=1)   # argmax is used for finding maximum value index

print(indices)