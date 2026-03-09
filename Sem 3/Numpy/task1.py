import random
import time

size = 200
mat_a = [[random.random() for _ in range(size)] for _  in range(size)]
mat_b = [[random.random() for _ in range(size)] for _  in range(size)]

result = [[0 for _ in range(size)] for _ in range(size)]
start_time = time.time()

for i in range(size):
    for j in range(size):
        for k in range(size):
            result[i][j] += mat_a[i][k] * mat_b[k][j]

end_time = time.time()
print(f"Execution time: {end_time-start_time}")