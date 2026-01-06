# We use the threading module in Python to run multiple tasks at the same time within a single program.
from threading import *     
class Hello(Thread):
    def run(self):
        for i in range(50):
            print("Hello")
class Hi(Thread):
    def run(self):
        for i in range(50):
            print("Hi")
t1 = Hello()
t2 = Hi()
t1.start()
t2.start()
