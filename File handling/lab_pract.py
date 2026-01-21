with open("student.txt","w") as f:
    name = input("Enter name:  ")
    f.write(f"Name: {name}\n")

with open ("student.txt","r") as f:
    data = f.read()
    print("File Concepts:\n",data)
        

print()
with open("student.txt","a") as f:
    name = input("Enter name: ")
    f.write(f"{name} is a good student.He work hard daily and do every works at a regualr time")