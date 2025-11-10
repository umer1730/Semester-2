# user defined functions
# def functionname()
def sum(a,b):
    return a + b
sum = sum(10,20)
print(sum)

# hello function
def hello():
    print("hello")
hello()

# print length of the list
def printlenlist(list):
    print(len(list))
list1=[1,2,3.4,5]
list2=["red","blue"]
printlenlist(list2)
printlenlist(list1)

# print elements of the list in one line
def list_print(list):
    for i in range(0,len(list),1):
        print(list[i],end=" ")
list1=[1,2,3,4,5]
list_print(list1)

print()
#Module : math_ops.py
def add(a,b):
    return a+b
print(add(5,3))
def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))    
