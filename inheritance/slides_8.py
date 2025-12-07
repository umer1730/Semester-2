class Grand_parent:
    def family_name(self):
        return "Smith"
class Parent(Grand_parent):
    def parent_method(self):
        return "from parent"
class Child(Parent):
    def child_method(self):
        return "from child"
child = Child()
print(child.family_name())
print(child.parent_method())
print(child.child_method())

print()
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
class Car(Vehicle):
    def __init__(self,brand,doors):
        super().__init__(brand)
        self.doors = doors
car = Car("Toyota",4)
print(car.brand)
print(car.doors)

print()
class Shape:
    def __init__(self,name):
        self.name =  name
        self.area = 0
    def calculate_area(self):
        return self.area
class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius
        self.area = 3.14*radius*radius
class Triangle(Shape):
    def __init__(self,name,base,height):
        super().__init__(name)
        self.base = base
        self.height = height
        self.area = 0.5*base*height
    def display_info(self):
        return self.name,self.calculate_area()
Circle1 = Circle("cir1",5)
print(Circle1.calculate_area())

Tri1 = Triangle("Tri1",5,5)
print(Tri1.display_info())
print()
circle = Circle("Red",5)
triangle = Triangle("Green",3,4)
shapes = [circle,triangle]
print("===Common Behaviour===")
for shape in shapes:
    area = shape.calculate_area()
    print(f"Area: {area}")
print("\n===Unique Behaviuor===")
print(triangle.display_info())

print()
class Printer:
    def __init__(self,model):
        self.model = model
    def print_document(self,document):
        print(f"Printing: {document}")
    def status(self):
        return f"Printer {self.model} is ready"
class Scanner:
    def __init__(self,resolution):
        self.resolution = resolution
    def scan_document(self):
        print(f"Scanning at {self.resolution} DPI")
        return "Scanned image"
    def status(self):
        return f"Scanner {self.resolution}DPI is ready"
class Fax_Machine:
    def __init__(self,number):
        self.number = number
    def send_fax(self,document):
        print(f"Faxing to {self.number}: {document}")
    def status(self):
        return f"Fax Machine {self.number} is ready"
class AllInOnePointer(Printer,Scanner,Fax_Machine):
    def __init__(self,model,resolution,number):
        Printer.__init__(self,model)
        Scanner.__init__(self,resolution)
        Fax_Machine.__init__(self,number)
    def test_All_func(self):
        self.print_document("Test Page")
        self.scan_document()
        self.send_fax("Important Doc")
office_device  = AllInOnePointer("OfficeJet 5000",1200,"555-0123")
print("===Testing All Features===")
office_device.test_All_func()
print("\n===Individual Operations===")
office_device.print_document("Report")
scanned  = office_device.scan_document()
office_device.send_fax(scanned)

print()
class A:
    def process(self):
        print("A.process")
class B(A):
    def process(self):
        print("B.process")
        super().process()
class C(A):
    def process(self):
        print("C.process")
        super().process()
class D(B,C):
    def process(self):
        print("D.process")
        super().process()
d = D()
d.process()

print()
class A:
    pass
class B(A):
    pass
class C(A):
    pass
print(C.mro())
print(D.__mro__)

print()
class A:
    def process(self):
        print("A.process")
class B(A):
    def process(self):
        print("B.process")
        super().process()
class C(A):
    def process(self):
        print("C.process")
        super().process()
class D(B,C):
    def process(self):
        print("D.process")
        super().process()
d = D()
d.process()