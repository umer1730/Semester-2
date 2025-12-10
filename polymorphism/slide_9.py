class A:
    pass
class  B:
    pass
class C(A):
    pass
class D(A):
    pass
class E(A):
    pass
class F(C,D):
    pass
class G(D):
    pass
class H(E,B):
    pass
class I(F,G):
    pass
class J(G,H):
    pass
class K(I,J):
    pass
# print(K.__mro__)
print([cls.__name__ for cls in K.__mro__])
print()
class A:
    pass
class B:
    pass 
class C(A):
    pass
class D(A):
    pass
class E(C):
    pass
class F(D):
    pass
class G(E,B):
    pass
class H(F,C):
    pass
class X(G,H):
    pass
print([cls.__name__ for cls in X.__mro__])

print()
class A:
    pass
class B:
    pass
class C(A):
    pass
class D(A):
    pass
class E(B):
    pass
class F(C,D):
    pass
class G(D):
    pass
class H(E,B):
    pass
class I(F,G):
    pass
class J(H,G):
    pass
class K(I,J):
    pass
print([cls.__name__ for cls in K.__mro__])

print()
_internal_helper_function = lambda x:x * 2 
print(_internal_helper_function(5))   # 10

def public_function():
    return "This is public"
class Myclass:
    _protected_attr = 100
    public_attr = 200
print(public_function())   # This is public

print()
class Parent:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private= "Private"
    def show_all(self):
        print(self.public)
        print(self._protected)
        print(self.__private)
class Child(Parent):
    def check_access(self):
        print(self.public)
        print(self._protected)
       # print(self.__private) but we can access when we find show_all method
child = Child()
child.check_access()
child.show_all()

print()
class AccessDemo:
    def __init__(self):
        self.public_data = "Public"
        self._protected_data = "Protected"
        self.__private_data = "Private"
    def public_method(self):
        print("Public method")
    def _protected_method(self):
        print("Protected method (internal)")
    def __private_method(self):
        print("Private method (mangled)")
class SubclassDemo(AccessDemo):
    def __init__(self):
        super().__init__()
    def test_inheritance_access(self):
        print(f"Public Date: {self.public_data}")
        print(f"Public Method: {self.public_method()}")

        print(f"Protected Data: {self._protected_data}")
        print(f"Protected method: {self._protected_method()}")

        # print(f"Private Data: {self.__private_data}")  we can not access private attribute
        # print(f"Private Data: {self.__private_method()}")
obj = SubclassDemo()
obj.test_inheritance_access()

print()
class Animal:
    def speak(self):
        return "some animal sound"
    def move(self):
        return "moving somehow"
class Dog(Animal):
    def speak(self):
        return "Woof!"
    def movev(self):
        return "Returning on for legs"
class Fish(Animal):
    def speak(self):
        return "Blub Blub"
    def move(self):
        return "Swimming in water"
animals = [Dog(),Fish(),Animal()]
for animal in animals:
    print(f"Sound: {animal.speak()}, Movement: {animal.move()}")

print()
class Abc:
    def fncn(self):
        print("Parent class")
class xyz(Abc):
    def fncn(self):
        print("Child class")
obj = xyz()
obj.fncn()

print()
class Animal:
    def speak(self):
        return "The animal makes a sound"
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} The cat says Meow."
animals = [Animal(),Dog(),Cat()]
print("...Calling the same method on diferrent objects...")
for creature in animals:
    print(f"{creature.__class__.__name__}: {creature.speak()}")

print()
def area(length,width = None):
    if width is None:
        return length * length
    else:
        return length * width
print(area(4))
print(area(4,5))

print()
def display_info(*args):
    if len(args) == 1:
        return f"Displaing ID: {args[0]}"
    elif len(args) == 2:
        return f"Displaying Name: {args[0]}, Age: {args[0]}"
print(display_info(101))
print(display_info("Bob",30))

print()
x = 10
y = 5
name1 = "Ali"
print(x+y)
print(x-y)
print(name1)
# class Abc:
#     pass
# obj1 = Abc()
# obj2 = Abc()
# print(obj1 + obj2)

print()
class Abc:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __add__(self,other):
        return f"{self.name} and {other.name}"
    def __str__(self):
        return f"The object {self.name} belongs to class {self.__class__.__name__} with age {self.age}"
obj1 = Abc("obj1",30)
obj2 = Abc("obj2",32)
x = obj1 + obj2
print(x)
print(obj1)