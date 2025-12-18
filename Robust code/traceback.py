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


file_handle =  None
try:
    file_handle = open("config.txt","r")
    data = file_handle.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Starting the file read process")
finally:
    print("Execution complete.")
