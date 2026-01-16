from abc import ABC,abstractmethod
class Animal:
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Woof!")
class Cat(Animal):
    def sound(self):
        print("meow!")
c= Cat()
c.sound()
d = Dog()
d.sound() 


print()
class PaymentProcessor:
    @abstractmethod
    def pay_method(self,amount):
        pass
class Credit_card(PaymentProcessor):
    def pay_method(self, amount):
        print(f"Paid with credit card: ${amount}")
class Paypal(PaymentProcessor):
    def pay_method(self, amount):
        print(f"Paid wit pay pal: ${amount}")
c = Credit_card()
c.pay_method(100)

p = Paypal()
p.pay_method(100)

print()
from abc import ABC, abstractmethod

# Abstract Base Class
class SortAlgorithm(ABC):
    @abstractmethod
    def sort(self, numbers):
        pass
class QuickSort(SortAlgorithm):

    def sort(self, numbers):
        sorted_list = sorted(numbers)   # using Python's Timsort as quick implementation
        print("Quick Sort:", sorted_list)
from abc import ABC,abstractmethod
class Sort(ABC):
    @abstractmethod
    def sorting(self, numbers):
        pass
class qsort(Sort):
    def sorting(self, numbers):
        print("Quick Sort:", sorted(numbers))
class msort(Sort):
    def sorting(self, numbers):
        print("Merge Sort:", self.merge_sort(numbers))
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr       
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])       
        return self.merge(left, right)
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

c = qsort()
c.sorting([1, 3, 2])

c = msort()
c.sorting([1, 3, 2])


print()
class FruitBasket:
    def __init__(self,items):
        self.items = items
    def __len__(self):
        return len(self.items)
    def __getitem__(self,index):
        return self.items[index]
    def __contains__(self,fruit):
        return fruit in self.items
    
my_basket = FruitBasket(["Apple","Mango","Banana"])
print(f"Basket size: {len(my_basket)}")
print(f"First Fruit: {my_basket[0]}")
print(f"Is apple there? {'Apple' in my_basket}")
