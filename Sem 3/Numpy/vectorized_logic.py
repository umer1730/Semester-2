import numpy as np

data = np.array([10,-5,20,-1])

result = np.where(data < 0,0,data)

print(result)