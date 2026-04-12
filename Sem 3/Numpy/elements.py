import numpy as np
x = np.array([1,np.nan,5])
y = np.array([0,10,np.nan])

print(np.maximum(x,y))
print(np.fmax(x,y))


print()
print("repairing gaps")

data = np.array([1.5,np.nan,3.2,np.nan])
clean = np.where(np.isnan(data))
print(clean)