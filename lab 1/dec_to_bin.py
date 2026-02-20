def decNum(n):
    ans = 0
    pow = 1
    while n > 0:
        rem= n % 2  # which num i enter modulus and give ans
        n =n // 2
        ans += rem * pow
        pow *= 10
    
    return ans
print(decNum(42))


print()
print("Bitwise")
print("left shift")
print(10 >> 1)   # a / 2 ki power b

print("right shift")
print(8 << 1) 

print()
name = input("Enter name: ")
def personName(name):
    if name == "a":
        print("yes a is present")
print(personName(name))
