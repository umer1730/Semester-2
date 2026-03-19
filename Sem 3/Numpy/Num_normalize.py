import numpy as np
# X = np.random.standard_normal((100,5))
# arr = np.array((100,5))
# X_norm = (X-X.mean(axis=0)) / (X.std(axis=0))

# arr_norm = (arr - arr.mean(axis=0)) / (arr.std(axis=0))

# print(X_norm,"\n")

# print(arr_norm)

np.random.seed(42)
A = np.random.standard_normal((100,5))

A = np.random.uniform(0,100,(100,5))
A = np.random.randint(0,50,(100,5))
print(A.shape)

X_norm = (A-A.mean(axis=0)) / (A.std(axis=0))

print("Original matrix")
print(A)

print("Normalized matrix")
print(X_norm,"\n")

