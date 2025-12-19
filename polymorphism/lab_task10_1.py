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
