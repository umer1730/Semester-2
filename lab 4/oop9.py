class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book_name):
        self.books.append(book_name)
        print(f"{book_name} added to library!")
    def display_books(self):
        if not self.books:
            print("no books available")
        else:
            print("Available Books: ")
            for b in self.books:
                print("-",b)
    def borrow_books(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You borrowed {book_name}.")
        else:
            print("Book not found!")
library = Library()

while True:
    print("1. Add Book \n2.Display book \n3.Borrowed Book \n4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter book name: ")
        library.add_book(name)
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        name = input("Enter name: ")
        library.borrow_books(name)
    elif choice == "4":
        print("Exit")
        break
    else:
        print("Invalid try again")

print()
print("-----player----")
import random
class Player:
    def __init__(self,name):
        self.name = name
        self.health = 100
class Game:
    def fight(self,p1,p2):
        while p1.health > 0 and p2.health > 0:
            damage1 = random.randint(10,25)
            damage2 = random.randint(10,25)
            p1.health -= damage2
            p2.health -= damage1
            print(f"{p1.name} health: {p1.health}")
            print(f"{p2.name} health: {p2.health}")
            if p1.health <= 0 or p2.health <= 0:
                break
        if p1.health > p2.health:
            print(f"{p1.health} wins!")
        elif p2.health > p1.health:
            print(f"{p2.name} wins!")
        else:
            print("it's a draw")
p1= Player("Ali")
p2 = Player("Zain")
g = Game()
g.fight(p1,p2)

class Order:
    total_orders = 0
    def __init__(self,item,price):
        self.item = item
        self.price = price
        Order.total_orders -= 1
        print(f"Order created: {self.item} - Rs.{self.price}")
for i in range(3):
    item = input("Enter item name:")
    price = float(input("Enter item price: "))
    order = Order(item,price)
print(f"Total orders placed: {Order.total_orders}")

print()
print("----quiz-----")
class Quiz:
    def __init__(self):
        self.questions = {
            "What is the capital of France?":"Paris",
            "What is 5 * 6?":"30",
            "Who developed Python?": "Guido Van Rossum"
        }
        self.score = 0
    def start_quiz(self):
        for q,a in self.questions.items():
            ans = input(q+" ").lower()
            if ans == a:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! Correct answer is {a}")
        print(f"Your Final score: {self.score}/{len(self.questions)}")
quiz = Quiz()
quiz.start_quiz() 