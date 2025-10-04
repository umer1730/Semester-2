for i in [1,2,3]:
    print(i)

print("---------")
print()
for i in range(10):
    if i == 5:
        break
    print(i)

print()
for i in range(10):
    if i == 5:
        continue
    print(i)

print("----------")
print()
num = 5
while num > 0:
    print(f"Number: {num}")
    num -= 1

print("----------")
print()
# secret_number = random.randint(1,10)
# guess = 0
# print("I'm thinking of  a number between 1 and 10")
# while guess != secret_number:
#     guess = int(input("Guess the number: "))
#     if guess < secret_number:
#         print("Too low!TRy again.")
#     elif guess > secret_number:
#         print("Too high!Try again.")
# print(f"Congratulations! You guessed it.The number was {secret_number}")
numbers = [1,2,3]
squares = []
for n in numbers:
    squares.append(n**2)
# squares = [n**2 for n in numbers]
print(squares)

print("-------------")
print()
numbers = [1,2,3]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)

print("-------------")
print()
num = [n**2 for n in range(3)]
print(num)

print("-------------")
print()
def greet(name):
    print(f"Hello, {name}")
greet("ali")
greet("arslan")

print("-------------")
print()
def sum_all(*args):
    print(f"The arguments are a tuple: {args}")
    return sum(args)
print(sum_all(1,2,3,4))

print("-------------")
print()
def print_info(**kwargs):
    print(f"The keyword argements are a dictionary: {kwargs}")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
print_info(name="Ali", age = 25)

print("-------------")
print()

def get_data():
    name = "ali"
    age = 25
    return name,age
user_name,user_age = get_data()
print(f"Name: {user_name} Age: {user_age}")

print("------------")
print()

