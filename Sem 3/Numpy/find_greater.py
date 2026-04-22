import numpy as np

np.random.seed(0)
arr = np.random.randint(0,101,(10,10))
result = arr[(arr % 2 == 0) & (arr > 50)]
print(result)

print()
print("Replace value using indexing")
arr = np.array([-5,0,7,-2,3,0,9])

result = np.where(arr < 0,0,np.where(arr > 0,1,-1))
print(result)