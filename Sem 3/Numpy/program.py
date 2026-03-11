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
print("element wise")
arr = np.array([[1,2],[3,4]])
print(arr * arr)
print(arr + 10)

print()
print("indexing")
arr = np.arange(10)
print(arr[5:8])
arr[5:8] = 12
print(arr)

print()
print("views vs copies")
my_slice = arr[5:8]
my_slice = 12345
print(arr)

print()
print("multidimensional indexing")
arr2d = np.array([
[1, 2, 3],  # Row 0
[4, 5, 6],  # Row 1
[7, 8, 9]   # Row 2
])
# 1. Get Row 0, Column 2 (The number 3)
print(arr2d[0, 2])    
# 2. Get the whole Row 1 (The middle row)
print(arr2d[1, :])    
# Output: [4 5 6]
# Note: You can also just use arr2d[1], but [1, :] is clearer in AI code.

print()
print("multidimension slicing")
M = np.array([
    [10,11,12,13],
    [20,21,22,23],
    [30,31,32,33],
    [40,41,42,43]
])
print(M[1:3,1:3])

print()
print("-----filtering")
names = np.array(["Bob","Joe","Will","Bob"])
data = np.random.standard_normal((4,2))
filtered = data[names == "Bob"]
print(data,"\n")
print(filtered)

print()
print("Logical masks")
data[data<0] = 0
print(data,"\n")
mask = (names == "Bob") | (names == "Will")
print(mask)

print()
print("Transposing arrays------")
arr = np.arange(15).reshape((3,5))
print(arr.T,"\n")
#Dot product: X^T @ X
print(np.dot(arr.T,arr))

print()
print("Universal functions (Unary)------")
arr = np.arange(10)
print(np.sqrt(arr),"\n")
print(np.exp(arr)) #e^x

print()
print("Vectorized logic------")
arr = np.random.standard_normal((4,4))
# if val > 0 , return  2 else return -2
result = np.where(arr > 0,2,-2)
print(result)

print()
print("Statistics & Aggregation-------")
print(arr.mean()) #global mean
print(arr.sum(axis = 0)) # column totals
print(arr.mean(axis = 0)) #column wise mean
