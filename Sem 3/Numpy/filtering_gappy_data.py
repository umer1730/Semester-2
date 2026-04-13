import numpy as np

sensors = np.array([1.2,np.nan,4.5,np.inf])
clean = sensors[np.isfinite(sensors)]
print(clean)


print()
print("Capping")
data = np.array([10,-5,20,-1])
data[data > 10] = 10

print(data)
