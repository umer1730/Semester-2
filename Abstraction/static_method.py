#They do not receive self or cls as their first argument. They accept only the arguments explicitly passed to them
class MathOperations:
    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        return n * MathOperations.factorial(n-1)
print(MathOperations.add(5,3))
print(MathOperations.factorial(5))

print()
class Bike:
    @staticmethod
    def start():
        print("Bike started")
    @staticmethod
    def stop():
        print("Bike stopped")
Bike.start()
Bike.stop()