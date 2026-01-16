from abc import ABC,abstractmethod
class Item(ABC):
    def __init__(self,title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,value):
        self._title = value.title()

    @abstractmethod
    def display_info(self):
        pass

class Book(Item):
    total_books = 0
    def __init__(self,title,author,isbn):
        super().__init__(title)
        self.author = author
        if self.is_valid_isbn(isbn):
            self.isbn = isbn
        else:
            raise ValueError("Invalid ISBN format")
        Book._increment_count()
    @classmethod
    def _increment_count(cls):
        cls.total_books += 1
    
    @classmethod
    def get_library_stats(cls):
        return f"Total Books in library: {cls.total_books}"
    
    @staticmethod
    def is_valid_isbn(isbn):
        return isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()

    def display_method(self):
        return f"Book: {self.title} by {self.author} (ISBN: {seelf.isbn})"

try:
    b1 = Book("Python OOP","M. Usman Yousaf", "123456789")
    b2 = Book("Java OOP","Imran Yousaf", "1298765789")

    print(b1.display_info())
    print(Book.get_library_stats())

    print(f"Formatted Title: {b1.title}")
except Exception as e:
    print(f"Error: {e}")

