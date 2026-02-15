pets = ['cats','dogs','chicken']
animals = ['dogs','chicken','cats']
print(pets == animals)

print()
print("-----------------")
cat_1 = {
    "name":"Zophie",
    "species":"cat",
    "age":"8"
}
cat_2 = {
    "species":"cat",
    "age":"8",
    "name":"Zophie"
}
print(cat_1==cat_2)

print()
print("------------")
a = {1,2}
b = {3,4}
print(a.union(b))   # (a | b)

print()
print("------------")
a = {1,2,3}
b = {3,4}
print(a.intersection(b))    # (a & b)

print()
print("------------")
a = {1,2,3}
b = {3,4}
print(a.difference(b))  # (a - b)

print()
print("------------")
a = {1,2,3}
b = {3,4}
print(a.symmetric_difference(b))   # (a^b)

print()
print("----------")
text = "Python"
res = text[::-1]
print(res)

print()
print("------------")
for i in range(1,6):
    print(i)

print()
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

print()
r = range(10)
print(r[2])
print(r[:3])

print()
r = range(0, 10, 2)
print(6 in r)
print(7 in r)

print()
r = range(0, 10, 2)
print(len(r))

print()
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

print()
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

print()
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 

print()
cars = ["Volvo","Ford","Mazda","Mercedes"]
for i in cars:
  print(i)

print()
a = int(input("Enter no: "))
square = a**2
print("Square: ",square)

print()
n=int(input("Enter num: "))
for i in range(0,n):
  for j in range(i,0,-1):
    print(j,end=" ")
  print()