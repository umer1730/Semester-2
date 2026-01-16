from abc import ABC, abstractmethod
class FileSystemItem(ABC):
    @abstractmethod
    def get_size(self):
        pass
class File(FileSystemItem):
    def __init__(self, size):
        self.size = size
    def get_size(self):
        return self.size
class Folder(FileSystemItem):
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def get_size(self):
        return sum(item.get_size() for item in self.items)
f1 = File(10)
f2 = File(20)
folder = Folder()
folder.add(f1)
folder.add(f2)
print("Total Size:", folder.get_size())
