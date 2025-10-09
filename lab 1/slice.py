# List of numbers
numbers = [10, 20, 30, 40, 50, 60]

print()

# Extract first three elements
first_three = numbers[:3]
print("First three:", first_three)

print()

# Extract elements from index 2 to 4
middle = numbers[2:5]
print("Middle elements:", middle)

print()

# Extract last three elements
last_three = numbers[-3:]
print("Last three:", last_three)

print()

print("NEXT EXAMPLE")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every 2nd element
even_index_elements = nums[::2]
print("Every 2nd element:", even_index_elements)

print()

# Every 3rd element starting from index 1
custom_slice = nums[1::3]
print("Every 3rd element from index 1:", custom_slice)

print()

print("NEGATIVE SLICE")

letters = ['a', 'b', 'c', 'd', 'e', 'f']

# Slice from 2nd last to 4th last (reverse order)
slice_part = letters[-2:-5:-1]
print("Negative slice:", slice_part)


print()
print("-----------------")
def mul(a,b):
    return a * b
print(mul(a=2,b=3))

print()
print("-------------------")
def div(a,b):
    return a / b
print(div(a=12,b=2))

print()
print("-------------------")
def sub(a,b):
    return a - b
print(sub(3,2))