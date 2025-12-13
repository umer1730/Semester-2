class Circle:
    def __init__(self,radius):
        self._radius = radius
    @property
    def radius(self):
        print("Getting radius value")
        return self._radius
circle = Circle(5)
print(circle.radius)

print()
# class Circle:
#     def __init__(self,radius):
#         self._radius = radius
#     @property
#     def radius(self):
#         return self._radius
#     @radius.setter
#     def radius(self,value):
#         if value<0:
#             raise ValueError("Radius cannot be negative")
#         print(f"Setting radius to {value}")
#         self._radius = value
# circle = Circle(5)
# circle.radius = 10
# circle.radius = -5

print()
class Circle:
    def __init__(self,radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,value):
        self._radius = value
c = Circle(4)
print(c.radius)

class Circle:
    def __init__(self,radius):
        self._radius = radius
    def get_radius(self):
        return self._radius
    def set_radius(self,value):
        self._radius = value
    radius = property(get_radius,set_radius)