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

print()
number = 1
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number = })")
print("This line comes after the forced exception")

print()
number = 2
try:
    if number > 5:
        raise Exception
except:
    print(f"The number should not exceed 5")
print("This line comes after the forced exception")

print("----------")
print()
number = 10
try:
    if number > 5:
        raise Exception(f"The number should not exceed 5 ({number=})")
finally:
    print("This line comes after the forced exception")

print()
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The try except is finished")

print()
x = -1
if x < 0:
    raise Exception("Sorry,no numbers below zero")