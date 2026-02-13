# list of numbers
numbers = [10,20,30,40,50,60]
first_three = numbers[:3]
print("First three:",first_three)

print()

# middle numbers
middle = numbers[2:5]
print("Middle Numbers:",middle)

print()

# last numbers
last_three = numbers[-3:]
print("Last three:",last_three)

print()

# next example
print("----Next example----")
nums=[1,2,3,4,5,6,7,8,9]
every_index_elements = nums[::2]
print("Every index second elementds: ",every_index_elements)

print()

# third element
custom_slice =  nums[1::3]
print("Every third element from index: ",custom_slice)

print()

# negative numbers
print("---Negative slice---")
letters = ['a','b','c','d','e','f']
slice_part = letters[-2:-5:-1]
print("Negative slice: ",slice_part)

print()
for i in range(1,4):
    for j  in range(1,4):
        print(i*j)
    