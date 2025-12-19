class Book:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return self.x + other.x
    def __str__(self):
        return f"{self.x} book clas to combine pages"
b1 = Book(400)
b2 = Book(50)
print(b1+b2)
