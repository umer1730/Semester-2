for i in range(1,6,2):
    print(f"Number: {i}")

print()
print("-------next-------")

fruits = ['apple','banana','cherry']
for fruit in fruits:
    print(f"Fruit: {fruit}")

print()
print("------next--------")
for i in range(5,0,-1):
    print(f"Countdown: {i}")

print()
print("------next--------")
word = "python"
for char in word:
    print(f"Characters: {char}")

print()
print("------next-------")
numbers = [1,2,3]
squares = []
for n in numbers:
    squares.append(n**2)
print(squares)              # if i enter print by using index then it give me all output one by one

#vs
print()
squares = [n**2 for n in numbers]
print(squares)

print()
print("-----next-------")
numbers = [1,2,3]
doubles = [n*2 for n in numbers]
print(doubles)

# vs
print()
numbers = [1,2,3]
doubles  = []
for n in numbers:
    doubles.append(n*2)
print(doubles)          # if i enter print by using index then it give me all output one by one

print()
print("-------next--------")
numbers = [1,2,3,4]
events = [n for n in numbers if n % 2 == 0]
print(events)

# vs 
print()
print("----------------")
numbers = [1,2,3,4]
events = []
for n in numbers:
    if n % 2 == 0:
        events.append(n)
print(events)

print()
print("------next------")
numbers= [1,2,3,4,5]
filtered = [n for n in numbers if n % 2 ==0 and n > 2]
print(filtered)

# vs
print()
print("----------")
numbers = [1,2,3,4,5]
filtered = []
for n in numbers:
    if n % 2 == 0 and n > 2:
        filtered.append(n)
        print(filtered)

print()
print("------next--------")
numbers = [1,2,3]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)

# vs
print()
print("------------")
numbers = [1,2,3]
labels = []
for n in numbers:
    if n % 2 == 0:
        labels.append(n)
        print("Even")
    else:
        labels.append(n)
        print("Odd")

print()
print("----next-----")
text = "hello"
vowels = [c for c in text if c in 'aeiou']
print(vowels)

# vs
print()
print("---------------")
text = "hello"
vowels = []
for c in text:
    if c in "aeiou":
        vowels.append(c)
print(vowels)