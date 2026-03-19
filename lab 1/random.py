import random

random.seed(100)

def print_random():
    for i in range(20):
        print(random.randint(0,100),end=" ")
print_random()