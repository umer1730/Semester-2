def greet_students(message="Welcome to Python!", *names):
    print(message)
    for name in names:
        print(f"- {name}")
# Example calls
greet_students("Good morning!", "Ali", "Sara", "Ahmed")
greet_students()

print()
print("--------next------")

def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum
# Example call
nums = [4, 7, 9, 2, 5]
total, avg, max_val, min_val = calculate_stats(nums)
print("Numbers:", nums)
print(f"Total: {total}, Average: {avg}, Max: {max_val}, Min: {min_val}")


print()
print("--------next------")

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        print(f"Checking middle index {mid}: {arr[mid]}")  # To show the steps

        if arr[mid] == target:
            return f"Element {target} found at index {mid}"
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return f"Element {target} not found in the list"

# Example usage
numbers = [2, 5, 7, 10, 14, 18, 21, 27, 30]
print("Sorted List:", numbers)

# --- The code below requires user input ---
target_value = int(input("Enter the number to search: "))
result = binary_search(numbers, target_value)
print(result)

print()
letters = [
    ["A","B","C","D"],
    ["E","F","G","H"]
]
print(letters[0][2])

print()
letters = [
    ["A","B","C","D"],
    ["E","F","G","H"]
]
letters[0][0] = "Z"
print(letters[0][0])

print()
num = int(input("Enter number: "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")

print()
n = int(input("Enter number: "))
for i in range(0,n):
    for j in range(i+1):   
        print("*",end=" ")
    print()    