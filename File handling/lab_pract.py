with open("student.txt","w") as f:
    name = input("Enter name:  ")
    f.write(f"Name: {name}\n")

with open ("student.txt","r") as f:
    data = f.read()
    print("File Concepts:\n",data)
        