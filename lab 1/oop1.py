class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")
b1 = Book("Python","John")
b1.display()


print()
print("-------------")