print("Umer")
print("is my name")
print("Umer","is my name")
print(20)
print(20+30)

print()
#data types int,float,str,bool,none
v1 = 23
v2 = 34.3
v3 = "My age is"
v4 = False
v5 = None
print(type(v1))
print(type(v2))
print(type(v3))
print(type(v4))
print(type(v5))

# concatenation with comma
# case sensitive language
print(v3,v1)

print()
# arithmetic operators
a = 10
b = 30
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

print()
#logical operators
print((a>b) and (not(a==b)))
print(not b)
print(a or b)

print()
# assignment operators
a*=10
b+=b
print(a)
print(b)

print()
#type conversatio occurs automatically
a=10
b=24.4
print(a+b)
print(type(a+b))

#typecasting done automatically
a="20"
b=int(a)
print(type(a),type(b))

print()
#taking inputs from user
# input("enter your name")
a=input("Enter a number: ")
print(type(a))
a = float(input("Enter a number: "))
print(type(a))

print()
#topic:string
str1 = 'This is'
str2 = " apple"
str3 = str1 + str2 + '\nI want to eat it'
print(str3)
print(len(str2))
ch = str1[6]
print(ch)

print()
#slicing imp in ML
print(str2[0:len(str2)])
print(str1[:len(str1)])
print(str1[0:])
print(str1[2:len(str1)-1])

print()
#list or arrays
marks = [34,67,89,67.8,78]
print(len(marks))
print(marks[0])


print()
#python list contain different data types
items = [34.4,45.5,"Ali"]
print("type of single elements",type(items[0]))
print("type of single elements",type(items[1]))
print("type of single elements",type(items[2]))

print()
#slicing
print(marks[0:len(marks)])
print(marks[:len(marks)])
print(marks[0:])

print()
#lists are mutable and strings are not immutable
items=[34,45.5,"Ali"]
items[1]="good"
print(items[0:len(items)])

print()
# str = "i m good"
# str[2] = 'y'
# print(str)   # type error 

print()
# temperature converter
celcius = float(input("Enter temperature in C: "))
fahrenheit = (celcius * 9/5)+32
print(f"{celcius}C = {fahrenheit}F")