with open("demofile.txt","w") as f:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    place = input("Enter place: ")
    do = input("Enter work: ")

    f.write(f"What is your name: {name}\n")
    f.write(f"What is your age: {age}\n")
    f.write(f"Where do you from: {place}\n")
    f.write(f"What are you doing: {do}")