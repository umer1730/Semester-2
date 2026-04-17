import numpy as np

from scipy.signal import convolve2d

image = np.array([[1,2,3],[4,5,6],[7,8,9]])

kernel = np.ones((3,3)) / 9

blurred = convolve2d(image, kernel, mode = "same", boundary="fill",fillvalue=0)
print(blurred)