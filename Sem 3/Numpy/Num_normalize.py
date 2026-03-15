import numpy as np
X = np.random.standard_normal((100,5))
arr = np.array((100,5))
X_norm = (X-X.mean(axis=0)) / (X.std(axis=0))

arr_norm = (arr - arr.mean(axis=0)) / (arr.std(axis=0))

print(X_norm,"\n")

print(arr_norm)