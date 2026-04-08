import numpy as np
data = np.array([10,-5,20,-1])
mask = data < 0
print(mask)

print()
print("Filtering with masks")
data = np.array([10,-5,20,-1])
clean_data = data[data > 0]
print(clean_data)