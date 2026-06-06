import numpy as np
data = np.array([1,np.nan,3])

print(np.isnan(data)) # find not a number
print(np.isfinite(data))