import numpy as np

a = np.array([1,0,np.nan,np.inf])
print(a / 0)

print()
print("Equality trap")
x = np.nan
print(x  == np.nan)
print(x != x)

print()
print("Detection suite")
data = np.array([1,np.nan,np.inf,-0.5])
print(np.isnan(data))
print(np.isfinite(data))