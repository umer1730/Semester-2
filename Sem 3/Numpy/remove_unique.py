import numpy as np
A = np.array([
    [1,2],
    [3,4],
    [1,2],
    [7,8]
])

unq = np.unique(A, axis = 0)
print(unq)