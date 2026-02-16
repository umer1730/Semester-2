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