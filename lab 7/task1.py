def login_system(password="oop123", max_attempts=3):
    """Validate password with a maximum of 3 attempts"""
    for attempt in range(max_attempts):
        entered = input("Enter password: ")
        if entered == password:
            print("Access granted!")
            return True
        else:
            if attempt < max_attempts - 1:
                print("Wrong password. Try again.")
            else:
                print("Access denied. Too many failed attempts.")
    return  