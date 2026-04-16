import numpy as np

np.random.seed(42)
x = np.random.uniform(0,1,size=5)

W = np.random.standard_normal((3,5))

b = np.random.randint(1,5,(3,1))

# x = np.array((5,))
# W = np.array((3,5))
# b = np.array((3,1))

# print(x)
# print(W)
# print(b)

result = W @ x.reshape(1,5).T + b
print(result) 