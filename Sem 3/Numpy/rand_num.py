import numpy as np
A = np.random.randint(1,10,(5,5))
K= 3
threshold = 50

submatrices = []
for i in range(A.shape[0] - K + 1):
    for j in range(A.shape[1] - K + 1):
        sub = A[i:i+K, j:j+K]
        if sub.sum() > threshold:
            submatrices.append(sub)
print(submatrices)
