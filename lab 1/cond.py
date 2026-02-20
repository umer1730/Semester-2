a = 10
b = 20

if a == b:
    print("a and b are equal")
elif a > b:
    print("a is greater than b")
else:
    print("a is less than b")

a = int(input("Enter number: "))
b = int(input("Enter number: "))
if a == b:
    print("Both numbers are equal")
elif a > b:
    print("First number is greater then second")
else:
    print("Second number is greater then first")


print()    
print("---------smallest and largest----------") 
list = [1,2,0,33,46,82] 
largest = max(list)
smallest = min(list)
print(f"Numbers in the list {list}")
print(f"Largest numbers in the list {largest}")
print(f"Smallest numbers in the list {smallest}")


print()
print("------check palindrome-------")
str = input("Enter string: ")
if str == str[::-1]:
    print("yes palindrome")
else:
    print("No palindrome")


print()
print("-----count vowels------")
word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
found = False  
for ch in word.lower():
    if ch in vowels:
        found = True
        break
if found:
    print("yes")
else:
    print("no")


print()
print("--------check prime-------")
n = int(input("Enter numbers: "))
if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print("not prime")
            break
    else:
            print("prime")
else:
    print("not prime")


print()
print("---------fibonacci----------")
def fibonacci(n):
    sequence = []
    a,b= 0,1
    for i in range(n):
        sequence.append(a)
        a,b=b,a+b
    return sequence
n = int(input("Ente num: "))
print(f"Fibonacci: {fibonacci(n)}")



print()
print("---------new list---------")
def unique(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
numbers = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original list:", numbers)
print("Unique list:", unique(numbers))

print()
print("-------frequency-------")
sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}
for word in words:
    word = word.lower()  
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word frequencies:")
for word, count in frequency.items():
    print(word, ":", count)


print()
print("--------students highest marks--------")
students = {
    "Ali": 85,
    "arslan": 92,
    "saad": 78,
    "zain": 90,
    "Hassan": 88
}
highest_student = max(students, key=students.get)
highest_marks = students[highest_student]
print("Students and their marks:", students)
print(f"\nTop student: {highest_student} with {highest_marks} marks.")

print()
print("implicit abstraction class")

print()
print("use double backslash\\ and these print only one backslash")

print()
print("use single backslash\' and print only comma")

print()
print("use single backslash\'' and print inverted comma")

print()
print("use single backslash\t and make three tab s")

print()
print("use single backslash\n and make next line")


print()
num = [5,15,22,1,-15,24]
smallest = min(num)
largest = max(num)
# for i in range(0,6):
#     if (num[i] < smallest):
#         smallest = num[i]
print("Smallest index number is: ",smallest)
print("Largest index number is: ",largest)

print()
def numbers(num):
    for i in num:
        if i > 3:
            print(i)
print(numbers([1,3,4,7,8,9]))

print()
num = int(input("Enter num: "))
if num == 1:
    print("1")
if num == 2:
    print("2")
if num == 3:
    print("3")
if num == 4:
    print("4")