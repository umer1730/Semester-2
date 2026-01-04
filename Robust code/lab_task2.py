def read_file(filename):
    try:
        with open(filename,"r") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print(f"File {filename} not found")
read_file("nonoexistent.txt")
