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


