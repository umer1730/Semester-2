import numpy as np

# arr_1 = np.array([50,28,28])
# arr_2 = ([100,28,28])
A = np.random.standard_normal((50,28,28))
B = np.random.standard_normal((50,28,28))

print(A.shape,"\n")

C = np.stack((A,B), axis=1)
print(C.shape)
ver = np.vstack((A,B))

hor = np.hstack((A,B))

print()
print(ver)
print("hor\n")
print(hor)
