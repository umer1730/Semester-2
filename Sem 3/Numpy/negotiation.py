import numpy as np

data = np.array([10,-5,20,-1])
out_liers = data > 15
normal_data = data[~out_liers]

print(data)
print(normal_data)

print(out_liers)
