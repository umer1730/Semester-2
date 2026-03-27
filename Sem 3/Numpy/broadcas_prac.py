import numpy as np

A = np.array([1,2,3,4,5])

result = A + 10
print(result)

print()
print("Multiply matrix by scalar")
A = np.array([[1,2,3],[4,5,6]])
print(A * 5)

print()
print("Add two 1D arrays")
A = np.array([1,2,3])
B = np.array([4,5,6])
print(A + B)

print()
print("Add 1D array to 2D array")
A = np.array([[10,20,30],[40,50,60],[70,80,90]])
B = np.array([1,2,3])
print(A + B)
