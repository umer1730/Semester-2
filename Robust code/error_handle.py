while True:
    try:
        num = int(input("Enter number: "))
        result = 100/num
        print(f"Result: {result}")
        break
    except ValueError:
        print("Error: That was not a valid integer. Using default value 0")
    except ZeroDivisionError:
        print(f"Division by zero is not allowed.Error {ZeroDivisionError}")
    print("Division successfully")
    print()

print()
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


