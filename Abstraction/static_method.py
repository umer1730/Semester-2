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