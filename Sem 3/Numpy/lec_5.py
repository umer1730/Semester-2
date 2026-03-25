import numpy as np

A = np.array([1,2,3])
B  = 2.0
print(A * B)

print()
print("broadcasting 1D across 2D")
a = np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]])
b = np.array([[1,2,3]])
print(a+b)

print()
print("Stretching both arrays")
a = np.arange(4).reshape(4,1)
b = np.array([1,2,3]) ## Both stretch to fill the (4, 3) grid
print(a+b)

print()
print("Forcing compatibility with np.newaxis")
