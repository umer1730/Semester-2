import numpy as np
from numpy.linalg import inv

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

print()
print("Linalg module")
X = np.array([[1,2],[3,4]])

X_inv = inv(X)
print(X @ X_inv)

print()
print("Linalg solve")
# A represents the coefficients (the numbers in front of x and y)
A = np.array([[1, 1], [2, 4]])
# b represents the constants (the results of the equations)
b = np.array([5, 16])
# Solve for x and y
solution = np.linalg.solve(A, b)
print(solution) 

det = np.linalg.det(A)
print(det) 

eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
