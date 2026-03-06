import numpy as np
data = np.array([[1.5, -0.1, 3],[0,-3,6.5]])
print(data)

print()
print("ndim")
print(data.ndim)

print()
print("shape")
print(data.shape)

print()
print("size")
print(data.size)

print()
print("dtype")
print(data.dtype)

print()
print("array dim")
arr_1D = np.array([6,7,8,9.5,0,1])
arr_2D = np.array([[1,0],[0,1]])
arr_3D = np.array([[[1,0],[1,1]],[[0,1],[1,0]]])
print(arr_1D)
print(arr_2D)
print(arr_3D)

print()
print("creates an array of all zeros")
zeroes = np.zeros((3,6))
print(zeroes)

print()
print("ones")
ones = np.ones(10)
print(ones)
