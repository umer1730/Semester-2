class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.y
        return x,y 
    def __sub__(self,other):
       x =  self.x- other.x
       y =  self.y-other.y
       return x,y
    def __str__(self):
        return f"{self.x},{self.y}"
p1 = Point(2,3)
p2 = Point(3,4)
# print (p1*p2)
# print(p1-p2)

p3 =p1-p2
print(p3)

p4 = p1*p2
print(p4)

class CHeck:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __floordiv__(self,other):
        x  = self.x // other.x
        y  = self.y // other.y
        return x,y
    def __str__(self):
        return f"{self.x},{self.y}"
p1 = CHeck(2,3)
p2 = CHeck(6,5)
p3 = p1 // p2
print(p3)