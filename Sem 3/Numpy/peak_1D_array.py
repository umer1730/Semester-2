import numpy as np

arr = np.array([1,3,2,5,4,6,1])

peaks = np.where((arr[1:-1] > arr[:-2]) & (arr[1:-1] > arr[2:]))[0] + 1

print(peaks)