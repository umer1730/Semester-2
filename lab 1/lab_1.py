number_1 = 5
number_2 = 3
result = number_1 + number_2
print(result)

print("---------")
print()
celsius = float(input("Enter temperature in °C: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

print()
print("-------------")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a =", a, ", b =", b)
temp = a
a = b
b = temp
print("After swapping: a =", a, ", b =", b)

print()
n = int(input("Enter number: "))
i =2
while i <= (n-1):
    if n%i == 0:
        print("Not prime")
        break
    else:
        i += 1
        print("prime")
        break