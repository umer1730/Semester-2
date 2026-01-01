class Person:
    def __init__(self,name,id_no):
        self.name = name
        self.id_no = id_no
    def display_info(self):
        return f"Name: {self.name} \nID: {self.id_no}"
class Student(Person):
    def __init__(self,name,id_no,major):
        super().__init__(name,id_no)
        self.major = major
    def display_info(self):
        return f"Name: {self.name}\nID: {self.id_no} \nMajor: {self.major}"
class Faculty(Person):
    def __init__(self,name,id_no,department):
        super().__init__(name,id_no)
        self.department = department
    def display_info(self):
        return f"Name: {self.name} \nID: {self.id_no} \nDepartment: {self.department}"
    def assign_course(course_name):
        return f"{course_name} assigned to"
p = Person("Ali",22)
print(p.display_info())
s = Student("Arslan",134,"AI")
print(s.display_info())
f = Faculty("adeem",678,"AI")
print(f.display_info())
print(f.assign_course())

print()
class Communication:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def phone(self,number):
        print(f"{number} Confirms a call")
class Camera:
    def __init__(self,resolution_mp):
        self.resolution_mp = resolution_mp
    def take_photo(self):
        print(f"{self.resolution_mp} Confirms a photo capture")
class Fitness_tracker:
    def __init__(self,sensor_count):
        self.sensor_count = sensor_count
    def monitor_hr(self):
        print(f"{self.sensor_count} Confirms heart rate monitoring")
class SmartPhone(Communication,Camera):
    def __init__(self,brand,model,resolution_mp,storage_gb):
        Communication.__init__(self,brand,model)
        Camera.__init__(self,resolution_mp)
        self.storage_gb = storage_gb
    def stream_video(self):
        print("Confirms video streaming")
class SmartWatch(Communication,Fitness_tracker):
    def __init__(self,brand,model,sensor_count,battery_life_days):
        Communication.__init__(self,brand,model)
        Fitness_tracker.__init__(self,sensor_count)
        self.battery_life_days = battery_life_days
    def syn_data(self):
        print("Confirms data synchronization")

print("\n===/ Smart phone /===")
p = SmartPhone("Apple","Iphone 15","2556+1179 pixels","512 GB / 1 TB")
p.storage_gb
p.stream_video()

print("\n===/ Samrt watch /===")
w = SmartWatch("Apple","020","e74"," 12 hours")
w.battery_life_days
w.syn_data()

print("\n===/ Communication /===")
c = Communication("Samsung","S22")
c.brand
c.model
c.phone("0300-1234567")

print("\n===/ Camera /===")
cam = Camera(4567)
cam.take_photo()

print("\n===/ Fitness track /===")
ft = Fitness_tracker(5)
ft.monitor_hr()


print()
class Point:
    def __init__(self,x,y):
        self.x  =  x
        self.y = y
    def __mul__(self,other):
        x =self.x * other.x
        y =self.y * other.y
        return x,y
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return x,y
    def __str__(self):
        return f"{self.x},{self.y}"
p1 = Point(2,3)
p2 = Point(4,5)
p3 = p1*p2
print(p3)
p4 = p1-p2
print(p4)


print()
class Cart:
    def __init__(self,name,cart_cost):
        self.name = name
        self.cart_cost = cart_cost
    def __gt__(self,other):
        return self.cart_cost > other.cart_cost
    def __it__(self,other):
        return self.cart_cost < other.cart_cost
    def __eq__(self,other):
        return self.cart_cost == other.cart_cost
    def __str__(self):
        return f"Name of cart: {self.name},Total price: {self.cart_cost}"
cart1 = Cart("Laptop",12222)
cart2 = Cart("Computer",100000)
print(cart1 > cart2)
print(cart1 < cart2)
print(cart1 == cart2)

print()
print()
class Product:
    Tax_rate = 0.05
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def display_price_with_tax(self):
        final_price = self.price + (self.price * Product.Tax_rate)
        return final_price
    @classmethod
    def set_tax_rate(cls,new_rate):
        cls.Tax_rate = new_rate
    @staticmethod
    def is_valid_price(price):
        return price > 0
p = Product("laptop",12000)
print(p.display_price_with_tax())
Product.set_tax_rate(0.10)
print(p.display_price_with_tax())