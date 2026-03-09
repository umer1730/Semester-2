import numpy as np
import time

size = 200
matrix_a = np.random.rand(size,size)
matrix_b = np.random.rand(size,size)

start_time = time.time()
result = matrix_a @ matrix_b
end_time = time.time()

print(f"Execution timr: {end_time - start_time}")