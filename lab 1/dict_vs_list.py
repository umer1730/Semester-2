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