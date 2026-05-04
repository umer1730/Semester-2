import numpy as np

data = np.array([10,-5,20,-1])

result = np.where(data < 0,0,data)

print(result)

print()
print("Patching data")
raw_data = np.array([1,np.nan,3])
backup = np.array([0,99,0])

clean = np.where(np.isnan(raw_data),backup, raw_data)

print(clean)