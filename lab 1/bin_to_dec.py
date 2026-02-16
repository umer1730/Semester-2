def binToDec(n):
    ans = 0
    power = 0

    while n > 0:
        rem = n % 10          # take last digit (0 or 1)
        ans += rem * (2 ** power)
        n = n // 10
        power += 1

    return ans

print(binToDec(110010))
