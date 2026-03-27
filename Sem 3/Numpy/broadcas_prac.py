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


print()
print("Add column vector to matrix")
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([10,20,30]).reshape(3,1)
print(A+ B)

print()
print("Subtract row means")
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
row_mean = A.mean(axis=1).reshape(3,1)
print(A - row_mean)

print()
print("Normalize matrix using column max")
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
column_max = A.max(axis=0)
normaliized = A / column_max
# print(column_max)
print(normaliized)

print()
print("create multiplication table")
a = np.arange(1,6).reshape(5,1)
b = np.arange(1,6)
table = a * b
print(table) 

print()
print("Distance from origin for points")
points = np.array([[1,2],[4,5],[7,8]])
origin = np.array([0,0])
dist = np.sqrt(((points - origin)**2).sum(axis=1))
print(dist)
