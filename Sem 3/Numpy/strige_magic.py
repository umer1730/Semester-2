import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

arr = np.array([1,2,3,4,5,6,])
windows = sliding_window_view(arr,window_shape=3)

print(windows)

print()
print(arr.reshape(2,3))