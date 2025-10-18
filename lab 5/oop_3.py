class Database:
    def __init__(self,name):
        self.name = name
        print(f"Connection to {self.name}")
    def __del__(self):
        print(f"Connection closed")
db =  Database("mydb")
del db
        