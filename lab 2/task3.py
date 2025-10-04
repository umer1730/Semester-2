a=0
b = 1
for i in range(10):
    print(a)
    a,b=b,a+b   #0,1=1 0+1=1 then 1+1=2


print()    
print("----first ten natural numbers-------")    
for i in range(1,11):
    print(i)


print()
print("------table---------")
num = int(input("Enter num: "))
for i in range(1,11):
    table = num*i
    print(f"{num} x {i} = {table}")



print()
print("------to sum numbers-----")
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10         
    sum_of_digits += digit    
    num //= 10                
print("Sum of digits =", sum_of_digits)



print()
print("-------find factorial-------")
y = int(input("Enter num:"))
fact = 1
if y < 0:
    print("factorial is not defined")
elif y == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,y+1):
        fact *= i
        print(f"Factorial: {fact}")