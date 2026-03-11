import numpy as np

A = np.array([[5,4], [3,2]])

B = np.array([[1,2],[3,4]])

print(A + B,"\n")
print(A - B,"\n")
print(A * B,"\n")
print(A / B)

print()
print("infix operator")
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[3,2]])
C = A @ B # np.do()
print(C)

print()
print("transposing matrix")
arr = np.array([[1,2,3],[4,5,6]])

print(arr.shape)
# transpose it
print(arr.T)
# transpose shape
print(arr.T.shape)


