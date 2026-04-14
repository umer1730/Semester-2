import numpy as np
arr =  np.array([10,20,30,40,50])
print(arr)

arr = np.zeros((3,3))
print(arr)

arr = np.ones((4,4))
print(arr)

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)

print()
print(arr1.mean())
print(arr1.sum())
print(arr1.std())

print()
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.max())
print(arr.min())

print()
arr = np.array([1,2,3,4,5])
print(arr[0])
print(arr[4])
print(arr[1:4])
print(arr[::-1])

print()
b= np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(b[2, 1])
print(b[0])
print(b[:,1])
print(b[1:3, 1:3])


print()
a = np.array([12,5,8,130,44])
print(a[a>10])
print(a[a<20])
print(np.where(a>100,0,a))

print()
salary = np.array([45000,100000,23000,75000,80000])
print(salary[salary>75000])
print(np.mean(salary))
print(np.max(salary))
print(np.sum(salary<60000))

print()
arr = np.arange(1,26).reshape(5,5)
print(arr)
print(np.diag(arr))

print()
border = np.concatenate((arr[0,:],arr[-1,:],arr[1:-1,-1]))
print(border)

print()
a = np.arange(1,37).reshape(6,6)
sub = a[1:5, 1:5]
sub[0,:] = -1
sub[-1,:] = -1
sub[:,0] = -1
sub[:,-1] = -1

a[1:5, 1:5] = sub
print(a)

print()
A = np.array([[1,2],[3,4],[5,6]])
B = np.array([[7,8],[9,10]])
dist = np.sqrt(((A[:,None,:] - B[None,: , :]) **2).sum(axis = 2))
print(dist)