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

print()
print("empty")
arr = np.empty((2,3,2))
new_zeroes = np.zeros_like(arr)
print(new_zeroes)

print()
print("arange")
r = np.arange(15)
print(r)

print()
print("linspace")
l = np.linspace(0,1,5)
print(l)

print()
print("unsigned integers")
arr_int  = np.array([1,2,3], dtype=np.int32)
arr_float = np.array([1,2,3], dtype=np.float32)
print(arr_int)
print(arr_float)

print()
print("astype")
arr = np.array([3.5,4.6,7.6,8.2])
int = arr.astype(np.int32)
print(int)

print()
print()