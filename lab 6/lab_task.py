class Laptop:
    brand = "Generic"
    def __init__(self,model):
        self.model = model
lap1 = Laptop("X1")
print(lap1.model,lap1.brand)

print()
print("-----phone------")
class Phone:
    os = "Android"
    def __init__(self,model):
        self.model = model
phone1 = Phone("Redmi 12c")
print(phone1.model,Phone.os)  # same 


print()
print("----next----")
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age= age
stud = Student("Alpha",20)
print(stud.name,stud.age)

print()
print("-----isinstance------")
class Student:
    def __init__(self,name,age):
        if isinstance(name,str) and isinstance(age,int):
            self.name = name
            self.age = age
        else:
            print(f"Invalid input, {name} object not created\n")
            del self
stu1 = Student("Ali",20)
stu2 = Student("Adsbbccj1",10) #when you add commas in 10 then error 
stu3 = Student("123",30) # when you remove commas from 123 then also error
print(f"Student 1 name is {stu1.name}, aged {stu1.age}\n")
print(f"Student 2 name is {stu2.name}, aged {stu2.age}\n")
print(f"Student 3 name is {stu3.name}, aged {stu3.age}\n")


class Student:
    def __init__(self,name,age):
        while not(isinstance(name,str)and isinstance(age,int)):
            print("Invalid input.Re-enter correct data")
            print("String for name and int for age")
            name = input()
            age  = int(input())
        self.name = name
        self.age = age
        print(f"Object created!")
stu1 = Student("Ali",20)
#stu2 = Student("Aeeeed","20")  This will cause error
print(f"Student 1 name is {stu1.name}, aged {stu1.age}")
#print(f"Student 2 name is {stu2.name}, aged {stu2.age}")

print()
print("----del---")
class Student:
    def __init__(self,name):
        self.name= name
        print(f"{self.name} is created")
    def __del__(self):
        print(f"{self.name} is destroyed")
stud = Student("Bob")
stud2 = stud
del stud
del stud2

print()
x =10
y =3
result = f"The sum of {x} and {y} is {x+y}"
print(result)

num = [1,2,4,3]
print(min(num))
print()
num.sort(reverse=True)
print(num)
w="bndd,d "
print(len(w))

print()
numbers = [1,2,3]
squares = []
for n in numbers:
    squares.append(n**2)
print(squares)

print()
numbers = [1,2,3,4]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    print(evens)

print()
num = [n**2 for n in range(3)] 
print(num)   

print()
def greet():
    print("Hello!")
greet()

print()
class Solution:
    
    def pair_sum(self, nums, target):
        ans = []
        n = len(nums)
        i = 0
        j = n - 1

        while i < j:
            current_sum = nums[i] + nums[j]

            if current_sum > target:
                j -= 1
            elif current_sum < target:
                i += 1
            else:
                ans.append(i)
                ans.append(j)
                return ans

        return ans


nums = [2, 7, 11, 15]
target = 13

s = Solution()
ans = s.pair_sum(nums, target)

if ans:
    print(ans[0], ",", ans[1])
else:
    print("No pair found")
