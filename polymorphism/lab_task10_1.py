class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def __add__(self,other):
        add_1 = self.real + other.real
        add_2 = self.img + other.img
        return Complex(add_1,add_2)
    def num(self):
        print(f"{self.real}i, {self.img}j")
add_1 = Complex(9,5)
add_1.num()


print()
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
v1 = Vector(2,3)
v2 = Vector(4,5)
print(v1+v2)