#A traceback is an error report that Python displays when an exception occurs.
# it starts from bottom to top
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
def process_data(data):
    return calculate_average(data)
def main():
    data = []
    result = process_data(data)
    print(f"Average: {result}")
main()