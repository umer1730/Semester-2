from math import pi

class Shape:
    def area(self):
        print("Area cannot be find!")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi*self.radius**2

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self,base,heigth):
        self.base = base
        self.heigth = heigth
    def area(self):
        return 0.5 * self.base*self.heigth

shapes = [
    Circle(5),
    Rectangle(4,3),
    Square(4),
    Triangle(2,3)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area:", shape.area())
