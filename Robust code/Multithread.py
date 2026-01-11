# In Python, we use the sleep() function (from the time module) to pause the execution of a program for a specific amount of time.
from time import sleep
# We use the threading module in Python to run multiple tasks at the same time within a single program.
from threading import *     
class Hello(Thread):
    def run(self):
        for i in range(50):
            print("Hello")
            sleep(i)
class Hi(Thread):
    def run(self):
        for i in range(50):
            print("Hi")
            sleep(i)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2) # gap between 2 sec
t2.start()

