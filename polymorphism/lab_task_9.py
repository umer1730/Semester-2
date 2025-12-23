class Bird:
    def fly(self):
        print("Bird flying")
class Airplane:
    def fly(self):
        print("Airplane flyiing")
def let_it_fly(obj):
    obj.fly()
let_it_fly(Bird())
let_it_fly(Airplane())

print()
class Shapes:
    def area(self):
        print("cannot find")
class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
class Rectangle(Shapes):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
c = Circle(5)
print(c.area())

r = Rectangle(4,3)
print(c.area())


print()
class Database:
    def connect(self):
        print("Database")
class MySQl(Database):
    def connect(self):
        print("Connected to MySql")
class Sqlite(Database):
    def connect(self):
        print("Connected to sqlite")
d = MySQl()
d.connect()
s = Sqlite()
s.connect()

print()
class Number:
    def __init__(self,x,y):
        self.x= x
        self.y= y
    def __floordiv__(self,other):
        fdx= self.x // other.x
        fdy = self.y // other.y
        return Number(fdx,fdy)
    def __str__(self):
        return (f"floor div x = {self.x} , y = {self.y}")
fdx = Number(2,3)
fdy = Number(4,5)
print(fdx // fdy)
