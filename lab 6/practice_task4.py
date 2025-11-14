class Book:
    def __init__(self,title,author,price):
        self.__title = title
        self.__author = author
        self.__price = price
    @property
    def get_book(self):
        return self.__price
    @get_book.setter
    def get_book(self,new_price):
        if new_price >=0:
            self.__price += new_price
        else:
            print("Invalid price")
b = Book("Python","Guido",585)
print("Price: ",b.get_book)
b.get_book = 933
print("Updated price: ",b.get_book)

print()
class Counter:
    def __init__(self,counts):
        self.counts = counts
        print(f"Currents start")
    def __del__(self):
        print(f"Currents count in {self.counts}")
c= Counter(220)
del c