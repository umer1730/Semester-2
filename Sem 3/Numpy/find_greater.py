import numpy as np

np.random.seed(0)
arr = np.random.randint(0,101,(10,10))
result = arr[(arr % 2 == 0) & (arr > 50)]
print(result)