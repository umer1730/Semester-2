def mean(num):
    return sum(num) / len(num)
num=[1,2,3,4,5]
print(mean(num))

print("---median----")

def median(num):
    n = len(num)
    if n % 2 == 0:
        median = (num[n// 2-1] +num[n//2])/2   #agr even me hua to center wali 2 values ka mean lena ha
    else:
        median = num[n//2]
    return median
num = [1,2,3,4,5]
print(median(num))
